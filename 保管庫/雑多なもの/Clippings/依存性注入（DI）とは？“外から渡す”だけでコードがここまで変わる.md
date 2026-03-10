---
title: "依存性注入（DI）とは？“外から渡す”だけでコードがここまで変わる"
source: "https://qiita.com/HK_Reisfeld/items/d56f9704bc95ffc77e74"
author:
  - "[[HK_Reisfeld]]"
published: 2026-02-17
created: 2026-03-09
description: "はじめに ソフトウェア開発では、あるクラスやサービスが別の機能に依存することは避けられません。 たとえば「支払いサービス」が「決済ゲートウェイ」に依存するようなケースです。 ここでありがちな書き方が、依存するオブジェクトをクラスの中で直接 new してしまう方法です。 c..."
tags:
  - "clippings"
---
![](https://relay-dsp.ad-m.asia/dmp/sync/bizmatrix?pid=c3ed207b574cf11376&d=x18o8hduaj&uid=)

## Qiita Careers powered by IndeedPR

求人サイト「Qiita Careers powered by Indeed」では、エンジニアのあなたにマッチした求人が見つかります。

[求人を探す](https://careers.qiita.com/)

## はじめに

ソフトウェア開発では、あるクラスやサービスが別の機能に依存することは避けられません。  
たとえば「支払いサービス」が「決済ゲートウェイ」に依存するようなケースです。

ここでありがちな書き方が、依存するオブジェクトをクラスの中で直接 `new` してしまう方法です。

```python
class PaymentService:
    def __init__(self):
        # 依存を自分で作ってしまっている
        self.gateway = PaymentGateway()

    def process(self, amount: int):
        return self.gateway.charge(amount)
```

一見するとシンプルでわかりやすいように見えますが、この実装にはいくつかの問題があります。

- **テストが難しい** ： `PaymentGateway` をモックに差し替えられない
- **再利用性が低い** ：別のゲートウェイ（例：Stripe → PayPal）に切り替える時に、コードを書き換える必要がある
- **責務が不明確** ： `PaymentService` が「支払い処理」だけでなく、「依存の生成」の責務まで抱えてしまっている

これが、「依存を直接 `new` してしまうアンチパターン」になります。

FastAPI / Laravel / Rails / Spring Boot を例として、依存性注入（DI）の実装パターンを説明していきます。

## 依存性注入とは？

この問題を解決するのが、「 **依存性注入（Dependency Injection, DI）** 」です。  
「 **必要なものを自分で作らず、外から渡してもらう** 」 といった感じです。

車とガソリンで例えると、わかりやすいかと思います。

車は、「走る」ことに集中する機械です。  
でも、もし車が自分でガソリンを精製しなければならないとしたらどうでしょう？  
走る前に石油を掘り出し、精製し、燃料を作る…  
そんな車は現実的ではありません。

実際には、車はガソリンスタンドで燃料を「外から入れてもらう」ことで走れるようになっています。

**車（クラス）** は「走る」ことに専念し、 **ガソリン（依存）** は外部から供給される。  
これが、まさに依存性注入の考え方です。

## なぜDIが重要なのか

- **テストがしやすい** ：モックを注入できる
- **再利用性が高い** ：依存を差し替えて別の環境でも使える
- **保守性が上がる** ：クラスが自分で依存を作らないので責務が明確

つまり、DIは「 **車が走ることに集中できるように、燃料は外から供給する** 」仕組みと同じです。  
コードをシンプルに保ち、テストや保守を楽にします。

## 各フレームワークでの実装例

ここからは、代表的なフレームワークにおける実装とテスト例を見ていきます。

## FastAPI（Python）

```python
# services/payment_gateway.py
class PaymentGateway:
    def charge(self, amount: int):
        return {"message": f"Charged {amount} yen"}
```

```python
# dependencies.py
from services.payment_gateway import PaymentGateway
def get_gateway():
    return PaymentGateway()
```

```python
# main.py
from fastapi import FastAPI, Depends
from services.payment_gateway import PaymentGateway
from dependencies import get_gateway

app = FastAPI()

@app.post("/pay")
def pay(amount: int, gateway: PaymentGateway = Depends(get_gateway)):
    return gateway.charge(amount)
```

### テスト（pytest）

```python
from fastapi.testclient import TestClient
from main import app, get_gateway

def override_gateway():
    class FakeGateway:
        def charge(self, amount: int):
            return {"message": "fake charged"}
    return FakeGateway()

app.dependency_overrides[get_gateway] = override_gateway
client = TestClient(app)

def test_pay():
    response = client.post("/pay?amount=1000")
    assert response.json() == {"message": "fake charged"}
```

`app.dependency_overrides[get_gateway] = override_gateway` と書くことで、本来の `get_gateway` の戻り値を `FakeGateway` に差し替えることができます。

これにより、外部リソースに依存せずにモックを注入してテストを実行できるようになります。

## Laravel（PHP）

```php
// app/Services/PaymentGateway.php
namespace App\Services;
class PaymentGateway {
    public function charge($amount) {
        return "Charged {$amount} yen";
    }
}
```

```php
// app/Http/Controllers/PaymentController.php
namespace App\Http\Controllers;
use App\Services\PaymentGateway;

class PaymentController extends Controller {
    private $gateway;
    public function __construct(PaymentGateway $gateway) {
        $this->gateway = $gateway;
    }
    public function pay() {
        return response()->json($this->gateway->charge(1000));
    }
}
```

### テスト（PHPUnit）

（※Laravel9 以降では Pest も利用可能）

```php
use Tests\TestCase;
use App\Services\PaymentGateway;

class PaymentControllerTest extends TestCase
{
    public function testPayWithFakeGateway()
    {
        $this->app->bind(PaymentGateway::class, function () {
            return new class {
                public function charge($amount) {
                    return "fake charged";
                }
            };
        });

        $response = $this->post('/pay');
        $response->assertSee("fake charged");
    }
}
```

Laravel9以降は、型ヒントだけで自動で解決できます。  
Laravel8以前では、 `AppServiceProvider` で手動バインドが必要になります。

## Ruby on Rails

```ruby
# app/services/payment_gateway.rb
class PaymentGateway
  def charge(amount)
    "Charged #{amount} yen"
  end
end

# app/services/payment_service.rb
class PaymentService
  def initialize(gateway = PaymentGateway.new)
    @gateway = gateway
  end
  def process(amount)
    @gateway.charge(amount)
  end
end

# app/controllers/payments_controller.rb
class PaymentsController < ApplicationController
  def create
    service = PaymentService.new
    render json: { result: service.process(1000) }
  end
end
```

### テスト（RSpec）

```ruby
RSpec.describe PaymentsController, type: :controller do
  it "uses fake gateway" do
    fake_gateway = double("FakeGateway", charge: "fake charged")
    service = PaymentService.new(fake_gateway)

    allow(PaymentService).to receive(:new).and_return(service)

    post :create
    expect(response.body).to include("fake charged")
  end
end
```

**dry-containerを使った拡張**

`AppContainer.register(:payment_gateway) { FakeGateway.new }` で依存先を差し替えることによって、モックにすることが可能になります。

## Spring Boot（Kotlin）

```kotlin
// service/PaymentGateway.kt
package com.example.demo.service
import org.springframework.stereotype.Service

@Service
class PaymentGateway {
    fun charge(amount: Int) = "Charged $amount yen"
}
```

```kotlin
// controller/PaymentController.kt
package com.example.demo.controller
import com.example.demo.service.PaymentGateway
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RestController

@RestController
class PaymentController(
    private val gateway: PaymentGateway
) {
    @PostMapping("/pay")
    fun pay(): String = gateway.charge(1000)
}
```

### テスト（JUnit 5）

```kotlin
@SpringBootTest
@AutoConfigureMockMvc
class PaymentControllerTest(
    @Autowired val mockMvc: MockMvc
) {
    @MockBean
    lateinit var gateway: PaymentGateway

    @Test
    fun \`returns mocked charge\`() {
        whenever(gateway.charge(1000)).thenReturn("fake charged")

        mockMvc.perform(post("/pay"))
            .andExpect(status().isOk)
            .andExpect(content().string("fake charged"))
    }
}
```

`@MockBean` を付けることで、SpringのDIコンテナに登録されている `PaymentGateway` が、テスト時にはモックに差し替えられます。

これにより、実際の外部サービスやDBに依存せずに、モックを注入してテストを実行できます。

## まとめ

## アンチパターン

依存を直接 `new` してしまうと、テストが難しくなり、再利用性も低下し、クラスが本来の責務以上の役割を抱えてしまう。

## DIの本質

依存は「 **外から渡す** 」ことで、クラスは自分の責務に集中できる。  
これは「 **車は走ることに専念し、ガソリンは外から供給される** 」関係と同じである。

## フレームワークごとの違いと共通点

### FastAPI

- `Depends` で関数ベースのDI、 `dependency_overrides` でテスト差し替え

### Laravel

- サービスコンテナによる依存解決。
- 9以降は型ヒントだけで自動解決、8以前は手動バインドが必要

### Ruby on Rails

- 標準はコンストラクタインジェクション
- `dry-container` を導入すれば、Spring BootやLaravelに近い自動解決型DIも可能

### Spring Boot

- アノテーション＋DIコンテナで自動解決、テストでは `@MockBean` で差し替え

### 共通のメリット

- どのフレームワークでも、DIを導入することで **テスト容易性・再利用性・保守性** が大幅に向上する

## おわりに

依存性注入（DI）は、一見すると抽象的で難しそうに思えるかもしれません。  
しかし、本質はとてもシンプルで、「 **必要なものは自分で作らず、外から渡してもらう** 」 という考え方に尽きます。

フレームワークごとに書き方は異なりますが、DIのメリットは共通です。  
テストのしやすさ、再利用性、そして保守性の向上は、長期的に開発者を支え、システム全体の品質を確実に高めてくれます。

依存性注入は「 **高度なテクニック** 」ではなく、日常的に活かせる設計の基本です。  
ぜひご自身のプロジェクトでも、「 **外から渡す** 」発想を取り入れてみてください。

[0](https://qiita.com/HK_Reisfeld/items/#comments)

コメント一覧へ移動

X（Twitter）でシェアする

Facebookでシェアする

はてなブックマークに追加する

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2FHK_Reisfeld%2Fitems%2Fd56f9704bc95ffc77e74&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2FHK_Reisfeld%2Fitems%2Fd56f9704bc95ffc77e74&realm=qiita)