---
title: "Docker一強の終焉にあたり、押さえるべきContainer事情"
source: "https://zenn.dev/ttnt_1013/articles/f36e251a0cd24e"
author:
  - "[[Announcing OpenShift Origin – Open Source Code For Platform-as-a-Service (PaaS)]]"
published: 2023-04-03
created: 2026-03-09
description:
tags:
  - "clippings"
---
1470

58[tech](https://zenn.dev/tech-or-idea)

## 章立て

1. はじめに
2. Docker・Container型仮想化とは
3. Docker一強時代終焉の兆し
4. Container技術関連史
5. 様々なContainer Runtime
6. おわりに

## 1\. はじめに

Containerを使うならDocker、という常識が崩れつつある。軽量な仮想環境であるContainerは、開発からリリース後もすでに欠かせないツールであるため、エンジニアは避けて通れない。Container実行ツール（Container Runtime）として挙げられるのがほぼDocker一択であり、それで十分と思われていたのだが、Dockerの脆弱性や消費リソースなどの問題、Kubernetes（K8s）の登場による影響、containerdやcri-o等の他のContainer Runtimeの登場により状況が劇的に変化している。本記事では、これからContainerを利用したい人や再度情報の整理をしたい人に向け、Container Runtime界隈の状況についてまとめた。

## 2\. Docker・Container型仮想化とは

## 2.1. Dockerとは

![Docker](https://res.cloudinary.com/zenn/image/fetch/s--2_gD7lAC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://1000logos.net/wp-content/uploads/2021/11/Docker-Logo-768x432.png?_a=BACAGSGT "Docker")  
Containerへのアプリケーションのデプロイを自動化するためのツール。無料で利用できるオープンソース版のDocker CE（Community Edition）と有償のDocker EE（Enterprise Edition）が存在し、Docker DesktopというソフトウェアでContainerを取り扱うツールの本体であるDocker Engineや、Kubernetes等を取り扱うGUIを操作することができる。  
下図のように、Docker daemonというサーバーに対してDocker clientから操作するというServer-client型で動作する。デフォルトの設定ではDocker daemonはcontainerdという高レベルのContainer Runtimeを起動する。containerdはDocker imageを管理したり、Docker containerを起動・実行するrunCという低レベルContainer Runtimeを実行する（構成の詳細は [こちら](https://lethediana.sakura.ne.jp/tech/archives/overview-ja/2054/) ） [^1] [^2] 。

![Docker内部構成](https://res.cloudinary.com/zenn/image/fetch/s--a8jpxYry--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://lethediana.sakura.ne.jp/tech/wp-content/uploads/2023/03/f527d84598d47468495ba5ea8bd13a41.png?_a=BACAGSGT "Docker構成")  
*Docker内部構成*

## 2.2 Container型仮想化とは

Dockerが行っているContainerによる仮想化とはどういうものかについてまとめる。そもそも仮想化とは、実際には「ない」ものを、あたかも「ある」かのように扱えるようにする技術である。したがって、何を「ある」ように扱うかによって、その仮想化技術がどのような特徴を持っているのかを整理して理解することができる。コンピュータの仮想化技術は、下記の5つのレベルに分けて考えることができることが知られている [^3] 。

1. Instruction Set Architecture（ISA） Level
	- CPUの命令セットを仮想化
	- 例：32bit Windowsの命令を64bit Windowsでも動くようにする技術
2. Hardware Abstraction Layer（HAL） Level
	- I/Oデバイスやメモリなどの物理デバイスとOSの間を仮想化
	- 例：Hypervisorを用いた仮想マシン（Virtural Machine）
3. Operating System（OS） Level
	- OSとアプリケーションの間を抽象化するための仮想化
	- 例：Container
4. Library Level
	- ユーザーとライブラリ間を仮想化
	- 例：Windowsのプログラムが呼び出すライブラリをMacのライブラリに読み替えて動かす技術
5. Application Level
	- 一つのアプリケーションのみを仮想化
	- 例：アプリケーションを外部のライブラリに依存せずに動かす技術

Container型仮想化はOSレベルの仮想化にあたり、これによりOSとアプリケーションの間を抽象化することができる。すなわちOSレベルの仮想化技術とは、kernelが複数のuserspaceのインスタンスを有してあたかも全く別の実行環境でプロセスを動作させているかのような状況を作り出す技術といえる。  
これを用いることで、OS上で隔離された環境を作ることができるため、実際は一つの物理マシンしか存在しなくても、複数ユーザーがあたかも複数のPCを操作している環境を得たり、アプリケーションをあたかもそれ専用のマシンで実行しているような環境を実現することができる。Hypervisor等を用いたHALレベルの仮想化でも同様のことが可能だが、より軽量な動作ができることが最も大きなメリットといえる（その他のレベルの仮想化についての詳細は [こちら](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/2040/) をご参考）。

> ![Hypervisor vs. Container virtualization design](https://res.cloudinary.com/zenn/image/fetch/s--qM1fkEg0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://cloudacademy.com/wp-content/uploads/2015/09/12.jpg?_a=BACAGSGT "Hypervisor vs. Container virtualization design")  
> *Hypervisor vs. Container virtualization design*  
> *引用： [Container Virtualization: What Makes It Work So Well?](https://cloudacademy.com/blog/container-virtualization/)*

## 3\. Docker一強時代終焉の兆し

Container技術をリーディングしてきたDockerがこれから一切使えなくなるとは考えにくいが、唯一解ではなくなってくる兆しが見えてきている。本章では、いくつかの例を紹介する。 [^4]

## 3.1. Docker desktopのライセンス形態

Visual StudioやUnityなど、有料ライセンスのみだったソフトウェアが無料で利用できるライセンスを持つようになることは、新規ユーザーの参入を増加させる効果が見込めるが、Dockerの場合はオープンソースだったソフトウェアの有償版（Docker EE）を提供するというビジネスを展開している。Dockerは前章で触れたように、2017年にこの戦略を打ったが、Kubernetesの普及により売り上げが伸び悩み、2019年にMirantisがDocker EEの事業を買収する運びとなった [^5] [^6] 。2023年現在、Dockerの主要有料製品はDocker DesktopとコンテナレジストリサービスであるDocker Hubのサブスクリプションである [^7] 。Personal用途のみ無料という価格設定のため、ある程度の規模の企業がDockerでContainerを管理したい場合はDocker Desktopのライセンス料を支払って利用することが第一の候補となる。しかし、実際のところ仮想化技術に疎い企業がこれをする場合、Container技術の優位性を説明して納得させることは難しい場合が多く、有料であることが足かせになってしまうこともしばしばあり、他のオープンソースのContainer Runtimeに流れる可能性は否めない（Docker CEはオープンソースで運営されているため、WindowsでWSLを立ち上げ、実質無償でDocker Engineを利用することは可能である）。

## 3.2. Dockerの脆弱性

Dockerのセキュリティが問題として挙げられることがしばしばあり [^8] 、2020年に「Dockerはサイバー犯罪者の主な標的である」としたレポートも存在した [^9] （Docker、Kubernetes専用のマルウェアも一つのトレンドとなった）。  
脆弱性の例として、Dockerを利用するとデフォルト設定でContainerはrootとして実行されることが挙げられる。rootユーザーでContainerを実行すると、Containerホストに必要以上の権利が与えられてしまう。したがって、万が一Containerに脆弱性があり（Container内で実行しているアプリが堅牢でも、Containerが基にしているImageに脆弱性がある可能性はしばしば問題点として挙げられる）、攻撃者がroot権限を手に入れてしまった場合、Containerを実行しているホストPCへのファイルアクセスやコマンド実行などの可能性が浮上する。また、Docker daemonがrootとして実行されることが問題とされることもある。Dockerも、DockerfileでContainerをrootユーザーが実行しない等の設定を加えたり、Docker daemonのrootlessモード [^10] を実装したりと対策を講じているが、Podmanをはじめとする他のContainer Runtimeに乗り換えることでDockerが抱えるセキュリティ問題が軽減されると考えられる場合もある [^11] 。

> **note**  
> セキュリティの他に、Dockerの機能的な弱点として、モニタリング機能やGUIベースのアプリが扱いにくいなどが挙げられることもある [^12]

## 3.3. KubernetesがDockerを非推奨

Kubernetesはリリース当初からDockerに公式で対応していたが、2022年4月をもってサポートを完全にストップし、Dockerを非推奨としている。これは前章で触れたCRIの登場により、Dockerを介さずともContainer Runtimeと直接やり取りできるようになったためである。すなわちDockerの場合で言えば、Dockerが利用しているcontainerdに直接働きかけることができるようになったということである。したがって、実はDockerを非推奨にしたといっても、Dockerを使っているとKubernetesが動作しないということではない（dockershimに依存したシステムを利用している場合はその限りではない） [^13] 。ただし、このKubernetesの対応によって、少なくともKubernetesの利用を前提としたシステムの場合はDockerを使う意味が薄くなっており、Dockerは開発者用ツールとしての色が濃くなったといって間違いはない。

## 3.4. Docker以外のContainer Runtimeの成長

現在、多くのContainer Runtimeがオープンソースで利用可能であり、Containerの実行形式もRuntimeによって様々な形が存在する。Dockerが完全に覇権をとったため、いずれもDockerをベンチマークにKubernetesとの連携性、軽量性、セキュリティの高さなど特色も持ち合わせており、環境・需要にあったContainerの実行環境が選択できるようになってきた（具体的にどのようなContainer Runtimeがあるかについては5章で詳細を述べる）。  
図にいくつかのContainer Runtimeの形式と、それぞれの関係性の概要についてまとめた（それぞれのツールのすべての設定をカバーしているわけではない）。ここでは、KubernetesのコンポーネントであるKubeletやContainer EngineからContainerを実行するまでの流れと、利用するツールの関係性を示している。図中では、Kata ContainerとgVisorをContainer Engineに含めているが、これらは低レベルのContainer Runtimeという位置づけでもしばしば描かれる（今回は後述の `kata-runtime` 、 `runsc` をそこに配置した）。  
それら加えて、Container Runtimeとは言えないが、Containerのような軽量の仮想環境を扱うためのツールも続々と出てきている（詳細は5章を参照されたい）。

![Container Runtime関係性](https://res.cloudinary.com/zenn/image/fetch/s--3EF8nw1W--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/4a8cc1f385c157250c87b99a.png%3Fsha%3D524e996fdd698f9fb6adb455c63b54edabb4f782)  
*Container Runtime関係性*

## 4\. Container技術関連史

本章では、OSレベルの仮想化技術がどのように発展してきたかを追い、Dockerの立ち位置を追う。

![Container技術関連史](https://res.cloudinary.com/zenn/image/fetch/s--_dBnKtxe--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/7735189819a351457ce5168f.png%3Fsha%3Dda0537d4201786aed74adc19780b74745f03d3a7)  
*Container技術関連史*

## 4.1. OSレベルの仮想化技術黎明期（1970~2004年ごろ）

1960から1970年頃、現在ほどコンピュータが世の中に溢れておらず高価で貴重品だった背景もあり、少ない物理マシンを複数のユーザーで共有するための仮想化技術が注目された。仮想化技術の中でも、OSレベルの仮想化の起源となるツールは、1979年のUnix version7で登場した、現在のプロセスとその子プロセス群に対してルートディレクトリを変更するシステムコール「 `chroot` 」であるといわれている [^14] 。このコマンドを実行することにより、プロセスごとにファイルアクセスを分離することができるため、各プロセスは、 **Jail** と呼ばれる仮想環境上で実行されているという状況を作り出す、すなわちOSの仮想化・分離化をすることが可能となる [^15] 。 `chroot` はのちの1982年に4.2BSDに正式に追加され、ユーザーがこの機能を利用できるようになった。  
この頃、システムの安定化を求めてアプリケーションの分散化が求められるようになったが、安価な小型コンピュータ（8ビットパソコン）の出現により、仮想化技術よりもマシンの台数を増やして対応する考え方が広がった。しかしながら、企業のマシン台数の増加により管理コストも増大し、再び仮想化技術が日の目を浴びることになる。そのような背景もあり、仮想化といえばHypervisor等のハードウェアをエミュレートするような考え方が花形だった中、 `chroot` による仮想化は、柔軟で複雑なプロセスにはやや不向きであることや、分離化されたはずのプロセス間のセキュリティホールが徐々に見つかってくるなど問題点が上がってきた。そんな中、新しいアプリケーションレベルでの仮想化技術として、2000年にFreeBSD 4.0で `jail` というツールが考案・導入された [^16] 。 `jail` で作成された仮想環境は同様に **Jail** と呼ばれ、各JailはIPアドレス、 `root` ディレクトリ等を割り当てらるため、 `chroot` による仮想環境よりも大幅に高機能な環境を実現することができた。

> **note**  
> プロセス仮想環境の文脈でJailというと、筆者が調査した限りではFreeBSDのJailを指す場合が多い。chrootで作成した仮想環境と、FreeBSDのそれを明確に区別するため、前者をchroot jails、後者をFreeBSD Jailsと呼ぶことがしばしばあるようである。

FreeBSD Jailsの登場まもなく、Linuxでもほぼ同等の仮想環境を構築するためのLinux VServerが2001年に導入された（Linux VServerはLinux Virtual Serverとは別プロジェクトであることに注意） [^17] 。Linux VServerでは、security contextと呼ばれるパーティションが作成され、その中の仮想化されたシステムを **Virtual Private Server** （ **VPS** ）と呼ぶ。  
そして2004年には、Oracle社のOSであるSolaris向けの仮想化ツール、Solaris Containers（ **Zone** と呼ばれるOSのインスタンスを持った仮想環境を扱う）の最初のパブリックベータ版がリリースされ、2005年にRHEL向けにOpenVZ（OpenVZにおける仮想環境のインスタンスは、 **VPS** 、 **Virtual Environment** （ **VE** ）、 **Container** （OpenVZのドキュメントでは **CT** と略される場合あり）などいくつかの用語で呼ばれる）がリリースされるなど、様々な環境でOSレベルの仮想化が可能になってきた。

## 4.2. Container誕生期（2004~2012年ごろ）

2004年頃からGoogle社でOSレベルの仮想化技術の開発に注力され、2006年にコンピュータリソース（CPU、RAM、ネットワーク、I/Oなど）の分離および制限のためのprocess containerと名付けられた機能開発を開始した [^18] 。このときprocess containerは、プロセスのコレクションであり仮想環境ではなかった。前節で軽く触れたように仮想環境の意味でContainerという用語が使われ始めていたため、混乱を避けるために翌2007年に **cgroup** （control groupの略）と改名され、さらにその翌年の2008年にLinux kernelに組み込まれた。

> **note**  
> 2007年5月のLinuxニュースサイトに紹介されたContainerの定義：
> 
> > A "container" is a group of processes which shares a set of parameters used by one or more subsystems.<sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-18">[18:1]</a></sup>
> 
> 現在でも用いられているcgroupの定義：
> 
> > A cgroup is a collection of processes that are bound to a set of limits or parameters defined via the cgroup filesystem.[^19]
> 
> 比較すると、両者が同じ概念であることがわかる。

そして同年2008年に、cgroupとLinux namespaceを用いた仮想環境、すなわち何のパッチも必要とせずLinux kernelのみで駆動可能な仮想環境として **LXC** （Linux Container）が登場した。  
2006年のころ、GoogleのCEOがクラウドについて言及したことや、パブリッククラウドの先駆けとなるAmazon Web Serviceがサービスを開始するなど、クラウドコンピューティング技術が普及し始めた。クラウドコンピューティング環境では、仮想マシン（Virtual Machine: VM）を利用することで、特にシステムの規模を柔軟に変更できる、オンプレ環境で必要だった管理の手間が省けるといったメリットが注目され、Webサービスだけではなく企業内システムのクラウド移行が徐々に進むことになる。  
そんな中2011年、LXCを用いた仮想環境を管理するためのAPIを提供するツールが、VMware社によるオープンソースのPaaS（Platform as a Service）であるCloud FoundryのWardenで提供され（Wardenのドキュメント上では仮想環境ではなく隔離環境と表記されている [^20] ）、2012年にRedHat社からOpenShiftというContainerの実行・管理ツールが発表 [^21] 、また2013年に、Googleが独自開発していたLXCと同様にcgroupとnamespaceを組み合わせたContainerシステムを **lmctfy** （Let Me Contain That For You）としてオープンソース化するなど [^22] 、OSレベルの仮想環境といえば **Container** による仮想化であるという認識が徐々に広がっていった。

> **note**  
> Googleでは2007年頃から社内インフラ用に隔離環境の需要があり利用していたが、インフラの再構築時に、Containerシステムを切り離すことが可能になり、それをオープンにすることを好意的に考えたため、lmctfyを公開するに至ったらしい [^23]

また、VM毎にOSのファイルや設定のためのデータを個別に管理する必要がある点や、それによるメモリーやストレージなどのリソースを大量に必要とする点などが本格的に問題視されはじめ、より軽量に動作するContainerがそのためのソリューションとして頭角を現していくことになる。そして、この頃までのContainerは、内部でOSを実行するVMと同じような管理をするSystem Containerと呼ばれる種のものがメインだったが、Containerごとに1つのプロセス・サービスを実行するApplication Containerが注目されてきた。

## 4.3. Container=Docker期（2012~2015年ごろ）

2012年頃にはIoT（Internet of Things）の流行や4Gの登場、さらにスマートフォンの所有率が10%に達する（下図参照）など、ソフトウェアの需要がますます高まりを見せていた。それに伴い、特にクラウドプラットフォームでの運用を考慮に置いたサーバーアプリケーションに関する開発および保守管理をより効率的に行うため、マイクロサービスアーキテクチャ、DevOps（DevelopmentとOperationsを組み合わせた造語）、CI/CD（Continuous Integration/Continuous Deliverry）といったスタイル・手法が普及していった。

> ![Global Smartphone User Base: % of World Population(1) (Source: Strategy Analytics, Inc.)](https://res.cloudinary.com/zenn/image/fetch/s--PFGhfm1J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://mms.businesswire.com/media/20210624005926/en/887635/4/SA%2BGraphic.jpg?_a=BACAGSGT "Global Smartphone User Base: % of World Population(1) (Source: Strategy Analytics, Inc.)")  
> *Global Smartphone User Base: % of World Population*  
> *引用：Strategy Analytics, Inc.*

> **note**  
> VMを用いたアプリケーション開発では、ハードウェアを用意・保守するコストがほぼなくなり従来の開発から大きく進歩したといえるが、テスト環境と本番環境の違いを保障することが非常に難しい、アプリケーションが共有しているリソース（メモリやDBなど）が適切に使われているかどうかの診断が難しい等、未解決のままの問題があった。これらに対して、アプリケーションごとに仮想化境が持てるApplication Containerに期待されていた。 [^24]

そのような状況で、2013年5月に、PaaSプロバイダであるdotCloud社が、 **Docker** というContainer Runtimeをオープンソース化した [^25] 。DockerによるContainerがJailと比べて最も画期的だった点は、Dokcerfileと呼ばれるファイルにContainerで実行するアプリケーションに必要な情報を記述する形式にしたことでContainerの共有を容易にしたことであると考えられ [^26] 、このことも後押ししてDockerプロジェクトは急成長し、Containerによる仮想化も一気に普及した。Dockerはリリース当初、デフォルトの実行環境としてLXCを使用していたが、2014年5月のバージョンアップでlmcfty由来のlibcontainerというGO言語で構成された環境を内部に取り込み、それでContainerを実行する方式に置き換えた（デフォルトの実行環境が変更されただけで、LXCで動作しなくなったわけではない。下図参照） [^27] [^28] 。  
そして同年7月には、Dockerの成長に伴い、dotCloud社は社名をDockerに変更し、dotCloudのサービスをcloudControl社に売却した。さらに11月に、GoogleがDockerコンテナを提供するGoogle Container Engine（GKE）を発表し [^29] 、AWSがDockerコンテナ対応のコンテナマネジメントサービスであるAmazon EC2 Container Serviceを発表するなど [^30] 、IT大手が次々にDockerに対応する環境を提供し始め、複数のDockerコンテナを取り扱いやすくする `docker-compose` のver1.0が10月にリリースされるなど、Container=Dockerという認識はますます強まっていった。

> ![Docker execdriver diagram](https://res.cloudinary.com/zenn/image/fetch/s--XI1JnkPA--/https://www.docker.com/wp-content/uploads/2014/03/docker-execdriver-diagram.png.webp?_a=BACAGSGT "Docker execdriver diagram")  
> *Docker execdriver diagram*  
> *引用： [Docker Desktop 0.9: Introducing Execution Drivers and libcontainer](https://www.docker.com/blog/docker-0-9-introducing-execution-drivers-and-libcontainer/)*

その他のContainer Runtimeとして、2014年12月にCoreOS社によるRocket（後のrkt） [^31] [^32] 、2015年2月にCanonical社によるLXDがリリースされるなど [^33] [^34] 、 **Container** による仮想化が全体的に盛り上がっていたが、Dockerのデファクトスタンダードとしての地位は揺るがなかった。  
様々なContainer Runtimeが出現する中、2015年6月にContainerのオープンな標準仕様を確立すべく、Docker、CoreOS、Google、AWSなどにより、 **Open Container Initiative** （ **OCI** ）が設立された（当初、Open Container Projectと呼ばれていたが、後にLinux Foundationプロジェクト傘下に入る） [^35] 。OCIは、Container Runtimeの仕様およびContainer Imageの仕様の策定に取り掛かったが、この際、Dockerが使用していたlibcontainerをContainer RuntimeのリファレンスとしてOCIにソースが提供され、さらにそれをDockerおよびRedhatの技術者によりOCIで定義するJSON型の仕様を読み取れるようにする等の機能を追加したlibcontainerのラッパーとして作成されたrunCという新たなツールもOCIに提供された [^36] [^37] [^38] [^39] 。 [runC](https://github.com/opencontainers/runc) はOCIの仕様に従ってContainerを取り扱うツールとして、今日でも管理されている。

> OCIの設立メンバーは下記の通り、錚々たる面々  
> CoreOS, Amazon Web Services, Apcera, Cisco, EMC, Fujitsu, Goldman Sachs, Google, HP, Huawei, IBM, Intel, Joyent, Mesosphere, Microsoft, Pivotal, Rancher Labs, Red Hat, VMware, Docker

## 4.4. Container=Docker+K8s期（2014~2018年ごろ）

Dockerの登場により、サービスを細かい要素にわけてContainer上で実行することで、従来のモノリシックアーキテクチャよりも柔軟なシステム構造であるマイクロサービスアーキテクチャを実現することができるようになった一方で、システム内に大量に配置されるコンテナを一つのグループ（しばしばクラスターと呼ばれる）として管理するための手段である **Container Orchestration** に関する需要があがってきた。  
前節のようにDockerが盛り上がりを見せていた2014年6月、Googleが社内でコンテナ管理のために使っていたプラッ  
トフォーム [Borg](https://research.google/pubs/pub43438/) およびOmegaを **Kubernetes** としてGO言語で再構築し、オープンソース化した [^40] [^41] 。

> **note**  
> Googleは、2015年1月のブログ記事で、  
> Kubernetesが運用オーバーヘッドが少ない、より優れたコンテナーベースのアプリケーションを作成するのに役立ち、それによってコンテナー採用の傾向が加速すると考えており、Kubernetesベースのアプリケーションの実行環境としてGoogle Cloud Platformがより多く使われるようになる [^42]  
> という戦略をイメージしていることを表明している。

また2015年10月に、Docker社はDockerコンテナのオーケストレーションツールとしてDocker Swarmをリリース（DockerはSwarmというシステムを2014年ごろからプレリリースしていた）、2016年7月には、クラスターのリソース管理を行なうMesosphere社のApache Mesos（2011年に発表 [^43] ）がDocker等のContainerに対応したversion1.0をリリースするなど [^44] 、オープンソースでContainer Orchestrationを行うための環境が出てきた。この頃に、AWSのAmazon ECS（Elastic Container Service）、RedHat社のOpenShiftがversion3でDockerおよびKubernetesを取り扱うように刷新されるなど、様々なOrchestrationツールが出現したが、Kubernetes、Docker Swarm、Apache Mesosの三強がデファクトスタンダードの地位を狙う状況となった。

> **note**  
> 前述の `docker-compose` も複数のコンテナを取り扱うための有用なツールであるが、単一のマシンでしか動かない点がDocker Swarmと大きく異なる点である。Kubernetes等その他のContainer Orchestrationツールでも、複数のマシンにまたがってクラスターのコンテナを配置することができる。

この中で最もシェアを取り、最も活発なオープンソースコミュニティとなったのはKubernetesである。その理由として、デプロイ機能、マルチクラウドに対応しやすい点などいくつかの要因が考えられる [^45] [^46] 。  
また、当初KubernetesはContainer RuntimeとしてDockerのみをサポートしていたが、CoreOSがrktもサポートに入れることを希望したことがきっかけとなり、様々なContainer RuntimeがKubernetes対応できるように2016年に **CRI** （Container Runtime Interface）と呼ばれるプラグインインターフェイスを導入し、前述のOCIを通じてOCID（OCI daemon）というプロジェクトを開始した [^47] [^48] 。OCIDはのちにCRI-Oに名称を変更されたプロジェクトで、これを利用するとOCIに準拠しているContainer RuntimeをKubernetesが直接実行できるようになるため [^49] 、Kubernetesが実質Container Runtimeに依存することがなくなり、さらにKubernetesコミュニティが独立して活動できるようになった。  
さらにKubernetesはクラウドコンピューティング環境で最新のアプリケーションを構築、デプロイ、および管理するアプローチである [Cloud Native Computing](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/1893/) の普及のために2015年に設立された [**CNCF（Cloud Native Computing Foundation）**](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/1884/) の最初のプロジェクトとして提供されたことも挙げられる。CNCFがコミュニティのハブとして機能したことで、CNCFの取り組みの中でKubernetesと親和性の高い周辺ツール（代表的なものはシステム監視ツールのPrometheus、サービスメッシュのIstioなど）が数多く生まれ、Kubernetesコミュニティを活性化したことで、サステナブルなツールであるという認知が進んだというわけである。  
Kubernetesのこのような動きを受けて、Dockerも2016年に高レベルなContainer Runtimeとして **containerd** （runcで実行するContainerのイメージ管理などを行う）をオープンソースとして分離し、翌2017年にCNCFプロジェクトに参加し [^50] 、containerdは2019年にGraduatedステージに認定された [^51] 。また、 `cri` というKubernetesのCRIを実装したcontainerdのプラグインを用いることで、Dockerを含むContainer RuntimeはKubernetesと直接相互運用が可能となった。この頃、Docker自体がrunCやcontainerdを用いてマイクロサービス化していることにも留意したい。

> **note**  
> CNCFの初期メンバーは、下記の通りである。  
> Google, CoreOS, Mesosphere, Red Hat, Twitter, Huawei, Intel, Cisco, IBM, Docker, Univa, VMware

そして、2017年10月のMicrosoft AKS（Azure Container Service）、2017年11月のAmazon EKS（Amazon Elastic Container Service for Kubernetes）の発表 [^52] 、2018年5月のGKE（Google Kubernetes Engine）の発表 [^53] により三大パブリッククラウドがすべてKubernetesに対応したことで、KubernetesがContainer Orchestrationのデファクトスタンダードであることを決定づけた。

## 4.5. Docker・Kubernetesの直近の動向（2017年ごろ以降）

2017年から2023年にいたるまで、DX（Digital Transformation）化の強力な流行と相まって、Kubernetesの成功により、Cloud Nativeというキーワードがさらに普及した。  
Dockerは、さらなるContainer技術普及のため2017年にDockerCon2017でLinuxの軽量なVMを作成するLinuxKitと、それを含むオープンソースプロジェクト **Moby** を発表し [^54] [^55] 、Githubのdocker/dockerリポジトリを [moby/moby](https://github.com/moby/moby) へ移行している。MobyはcontainerdやSwarmKitなどDockerで利用されているコンポーネントが含まれており、それらをレゴのように組み合わせて利用することで、環境に適したスタンドアロンなContainerシステムを作ることができる。Dockerというツールは、Mobyをベースとしたオープンソース版のDocker CE（Community Edition）と有償版のDocker EE（Enterprise Edition）に分離された。Mobyプロジェクトの今後の動向として、containerd、ビルドツール・Dockerfile、rootユーザー以外のdaemon起動、Mobyプロジェクトのテスト機能やより細かいコンポーネント化といった5項目がロードマップに上げられている [^56] 。  
さらに、プログラミング言語を抽象化する [WASM（WebAssembly）](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/2093/) をDockerを補完する技術として強調しており、サービスに必要なウエイトに応じてVM、Container、WASMを適切に選択することで、アプリケーションの質が向上するとしている [^57] [^58] 。Dockerの創設者の一人であるSolomon Hykes氏に、もし2008年にWASMとWASI（WebAssembly System Interfaceのこと。WASMがシステムリソースを利用するためのインターフェイス）が存在していたら、Dockerを作る必要はなかった [^59] 、と言わしめるほど、このWASMはDockerにとってインパクトが大きく、2022年のDocker Desktop 4.15へのアップデートでcontainerdの管理下でrunCの代わりにWASMのランタイムを操作するDocker+WASMのベータ版が利用可能となり [^60] 、 [docker/roadmap](https://github.com/docker/roadmap) のIssueの議論でさらに連携が強化されることが明かされている [^61] 。  
その裏で、DockerとともにContainer関連技術をリーディングするKubernetesも、さらに成長を続けている。  
一つ目の動向として、Kubernetes自体がより機能拡張している点が挙げられる。  
特に2017年6月のバージョンアップ（Kubernetes 1.7）により、KubernetesはCustom Controllerと呼ばれる機能を実装した [^62] 。これにより、2016年にCoreOSにより提唱されていたOperater Pattern [^63] を実現することが可能となった。このデザインパターンはKubernetes Operatorとして知られ、クラスターの運用方法（例えば、複数のコンテナ間でデータの同期やバックアップをどのタイミングでどうやってとるか等）をソフトウェアに組み込むパターンである [^64] 。開発者の頭の中にあるノウハウをソフトウェア化してOperatorとして作りこむことができるため、システムの自動化に非常に有用であり、ノウハウの共有もできるようになった。  
二つ目の動向として、Kubernetesをより使いやすくする動きもみられる。  
Kubernetes上でクラスターを管理しやすくするツールの代表例として、Helmが挙げられる。KubernetesとCloud Native Computingへ企業が移行するための支援を行っているDeis社（2017年4月にMicrosoftが買収 [^65] ）がオープンソースプロジェクトHelmを開発していた。Helmは、ユーザーがアプリケーションを簡単にパッケージ化してKubernetesにインストールできるようにすることに焦点を置かれたツールで、2016年にDeis、Googleが中心となり、Kubernetes Deployment ManagerというツールとHelmを統合してHelm2としてリリースされ、2018年にCNCFプロジェクトへ参加、さらに2019年にHelm3へアップデートすると2020年にはCNCFのGraduated認定を受けている。このHelmを用いると、KubernetesにデプロイするコンポーネントをChartと呼ばれる1つのグループとして扱うことができるため、管理コストが削減できる。これは様々なコンポーネントを含む、前述のOperatorの管理に非常に有用である。また、Kubernetesで構成されたシステム自体を管理しやすくするアプローチとして、Rancherが挙げられる。Rancherは、プライベートクラウドも含めてどのクラウドにもKubernetesクラスターをデプロイできるツールであり、GUIで管理できるため非常に直観的で人気を博している [^66] 。  
そして三つ目の動向として、Kubernetesの利用範囲を広げる動きがみられる。  
これまで、Kubernetesの主要な実行環境はクラウド上であったが、この有用性をIoT機器やエッジコンピューティング用デバイスにも持ってこようという動きがある [^67] 。この動向はリソース（メモリ、CPU等）に限りがあること、リアルタイム性が要求される可能性があること、セキュリティ対策、エッジ機器（組み込み機器）の多様性など、それ特有の課題が存在し、まだ浸透しきっているわけではない。しかしながら、2019年にRancherがエッジ用の軽量Kubernetesであるk3sをリリース [^68] 、2020年にCNCFでKubeEdgeと呼ばれるエッジでKubernetesを利用するためのツールがIncubateステージに認定されたりと [^69] 、エッジでKubernetesを利用するツールが現れてきた。また、GPUベンダーであるNVIDIAがNVIDIA GPU Operatorを発表 [^70] 、FPGA・SoCベンダーであるXilinx、IntelがKubernetes用のデバイスプラグインの提供を始めるなど [^71] [^72] 、各種ハードウェアベンダーもKubernetesへの対応に意欲的な姿勢を見せている。さらに、2022年6月にDocker Containerの実行を目的とした組込み用OSである [BalenaOS](https://www.balena.io/os) が登場 [^73] 、2022年9月にZEDEDA社によるエッジ向けOSであるEVE-OSがKuberentesをcontrol planeレベルでサポートする方向性を発表するなど（Kubernetesのcontrol planeについては [こちら](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/1991/) も参照） [^74] 、OSレベルでContainer利用に対応することで軽量化を測る試みも出てきている。  
研究分野では、 [ロボット](https://arxiv.org/pdf/2210.03936.pdf) や [Drone](https://arxiv.org/pdf/2301.13624.pdf) のコントローラをKubernetesで管理する例なども見られ、まだ発展途上ではあるが、非常に注目度が高いといえる。

## 5\. 様々なContainerの実行環境

本章では、押さえておくべきContainer Runtimeと、Container Runtimeとは呼べないが注目すべき軽量の仮想環境を実行するためのツールを挙げる。

## 5.1. 高レベルContainer Runtime

### containerd

![containerd](https://res.cloudinary.com/zenn/image/fetch/s--N5WtTCeZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://containerd.io/img/logos/footer-logo.png?_a=BACAGSGT "containerd")  
[containerd](https://containerd.io/) は、シンプルさ、堅牢性、および移植性に重点を置いた業界標準の高レベルのContainer Runtimeである。ここまでで触れたように、Docker社で開発が進められて2016年からDocker内部で使用された後 [^75] 、CNCFへ寄付されている。CNCFのProjectとしてGraduatedステータスを得ており、Sysdig 2022 Cloud-Native Security and Usage Reportによると、Dockerに次いで2位のシェアをとっていると報告されている [^76] 。ユーザーがcontainerdは単独で使用するのではなく、より大きいシステム（DockerやKubernetesなど）に組み込まれるように設計されている。基本的にdaemonプログラムとして動作し、低レベルのContainer RuntimeはデフォルトでrunCが使われており、Dockerに組み込まれていたという実績から信頼感もあり安定した人気を博している。

> ![containerd architecture](https://res.cloudinary.com/zenn/image/fetch/s--1yeyD_Yr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://github.com/containerd/containerd/raw/main/docs/historical/design/architecture.png?_a=BACAGSGT "containerd architecture")  
> *containerd architecture*  
> *引用： [containerd/containerd](https://github.com/containerd/containerd)*

### CRI-O

![CRI-O](https://res.cloudinary.com/zenn/image/fetch/s--GfXJxUI7--/https://github.com/cri-o/cri-o/raw/main/logo/crio-logo.svg?_a=BACAGSGT "CRI-O")  
[CRI-O](https://cri-o.io/) は、RedHat社によって2017年にリリースされた、Kubernetesに最適化された軽量のContainer Runtimeである。主な目標は、OpenShift Container Platform等のKubernetes実装のContainerエンジンとしてDockerから置き換えられることと置いており [^77] 、実際にDockerが利用しているContainer Runtimeであるcontainerdに比べてリソース消費が少なく効率的である <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-67">[67:1]</a></sup> 。CRI（Container Runtime Interface）にOCIのOを足してCRI-Oであると言われている <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-49">[49:1]</a></sup> 。KubernetesのPod内で安定に稼働することを強く意識されており、特にCRI-OのバージョンとKubernetesのバージョンが同じのとき対応が担保される（CRI-O 1.x.yとKubernetes 1.x.yは対応している）。もちろんOCI準拠であり、2019年にはCNCFのIncubatedステータスに承認された。そして、OpenshiftのデフォルトのContainer Runtimeということもあり、Sysdig 2022 Cloud-Native Security and Usage Reportによると、containerdに次いで3位のシェアをとっていると報告されている <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-76">[76:1]</a></sup> 。CRI-Oはcontainerdと同様にCRI-O daemonと呼ばれるdaemonを持ち [^78] 、CRI-O daemonがリクエストを受けると低レベルのContainer Runtimeを動作させ、各Containerにそれぞれ一つのconmonと呼ばれるContainerを管理・監視するプロセスを紐づける。したがってCRI-O daemonがダウンしても、conmonがログを収集するなど行うことができる点で、Dockerと構成が異なる [^79] 。低レベルのContainer RuntimeにはデフォルトでrunCが使われる。

> ![CRI-O architecture](https://res.cloudinary.com/zenn/image/fetch/s--yXeuxHcE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://cri-o.io/assets/images/architecture.png?_a=BACAGSGT "CRI-O architecture")  
> *CRI-O architecture*  
> *引用： [cri-o](https://cri-o.io/)*

### Podman

![Podman](https://res.cloudinary.com/zenn/image/fetch/s--Wadt0eHD--/https://podman.io/images/podman.svg?_a=BACAGSGT "Podman")  
[Podman](https://podman.io/) は、Red Hat社を中心に2019年にリリースされた軽量のContainer Runtimeである。Pod managerの略で、Kubernetesで導入されたPod（Containerのグループ）を管理するという思想をもつ（ロゴのモチーフはSelkieというアイルランドの人魚のような神話上の生き物で、Selkieはアザラシから人間の姿に変化することができるそうでロゴではアザラシの姿であると思われる。そしてSelkieはpodと呼ばれるグループを作る習性があることが由来している [^80] [^81] [^82] ）。libpodというContainerライフサイクル管理用のライブラリをベースにしており、低レベルのContainer RuntimeにはデフォルトでrunCが使われる [^83] 。Dockerが持つようなdaemonプロセスを持たず、CRI-Oと同様にconmonによりContainerを管理するため、動作が軽量で設定変更に柔軟に対応できるなどのメリットがある [^84] 。さらに、Rootlessモードを有するなど、セキュリティ性の高さも魅力の一つである。2022年にはPodman Desktopをリリースし、Dockerの対抗馬としての存在感をさらに強めている。

> ![Podman architecture](https://res.cloudinary.com/zenn/image/fetch/s--slfelT1k--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://developers.redhat.com/blog/wp-content/uploads/2019/01/podman-pod-architecture.png?_a=BACAGSGT "Podman architecture")  
> *Podman architecture*  
> *引用： [Podman: Managing pods and containers in a local container runtime](https://developers.redhat.com/blog/2019/01/15/podman-managing-containers-pods#podman_pods__what_you_need_to_know)*

> **note**  
> CRI-OやPodmanが軽量であるのは、ContainerやContainerイメージの管理に特化していることにも起因している。そこで、Containerのビルドツールである [Buildah](https://buildah.io/) や、Container Imageのコピー・検証ツールの [Skopeo](https://github.com/containers/skopeo) を合わせて利用することで機能を補完することがしばしば必要となる。  
> Red Hatは、BuildahでContainerをビルドし、PodmanでContainerを実行し、SkopeoでContainer Imageを転送するという、daemonレスに形成できるツールのエコシステムについて言及している [^85] 。  
> !["Buildah"](https://res.cloudinary.com/zenn/image/fetch/s--T1kuDhXN--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://buildah.io/images/buildah.png?_a=BACAGSGT "Buildah")  
> !["Skopeo"](https://res.cloudinary.com/zenn/image/fetch/s--WSE607Kt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://camo.githubusercontent.com/edb2cf198aad5b6bc776e245ac1f2a703b5aabcf11521bdb3a3b641b62dc8b0e/68747470733a2f2f63646e2e7261776769742e636f6d2f636f6e7461696e6572732f736b6f70656f2f6d61696e2f646f63732f736b6f70656f2e737667?_a=BACAGSGT "Skopeo")

## 5.2. 低レベルContainer Runtime

### runC

![runC](https://res.cloudinary.com/zenn/image/fetch/s--TmaVWP7K--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://www.cncf.io/wp-content/uploads/2020/08/runc-logo-5.png?_a=BACAGSGT "runC")  
[runc](https://github.com/opencontainers/runc) は、2015年にDockerからスピンアウトした、OCI仕様のLinux Containerを生成・実行するためのCLIツールである [^86] 。現在はOCIにメンテナンスされており、Go言語で記述されている。軽量で移植性が高く、containerdと同様にDockerに組み込まれてデフォルトで使用されていることから、実績と信頼の高いContainer Runtimeである。

### crun

![crun](https://res.cloudinary.com/zenn/image/fetch/s--_l0L67Ra--/https://github.com/containers/crun/raw/main/docs/crun.svg?_a=BACAGSGT "crun")  
[crun](https://github.com/containers/crun) は、2021年にversion1.0がリリースされた新しい低レベルのContainer Runtime。主にRed Hat社によってメンテナンスされている。runcとの大きな違いは、crunがc言語で記述されている点である。Go言語は、fork/execモデルを適切にサポートしていないなど、いくつかの問題点がありruncの開発では、機能させるために多くの巧妙なハックを追加しているが、それでもGo言語の制限による制約を受けていることを問題視している [^87] 。基本的にruncよりも軽量（runcのバイナリが15MB程度であるのに対し、crunは300kB程度。100個のContainerを実行させるのにruncが3.34秒かかったのに対し、crnは1.69秒しかかからなかった）であるが、2023年1月にリリースされたOpenshift 4.12でも、本番環境でcrunを使うことは非推奨とされている [^88] 。

### youki

![youki](https://res.cloudinary.com/zenn/image/fetch/s--6vpNlP6E--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://containers.github.io/youki/assets/youki.png?_a=BACAGSGT "youki")  
[youki](https://github.com/containers/youki) は、2021年にversion0.0.1がリリースされたRustで記述された低レベルのContainer Runtime。Rustは2020年にversion1.0がリリースされたプログラミング言語で、システムコールを利用するのにGo言語ほど複雑にならず、C言語よりメモリの安全性が担保される。Oracleが開発していた [railcar](https://github.com/oracle/railcar) をもとに、 [Toru Komatsu（うたもく）](https://twitter.com/utam0k) 氏が2021年3月にプライベートリポジトリで開発していたプロジェクトを公開 [^89] 、注目が集まった後 [^90] 、現在はPodmanやcrunも所属するContainersというグループに所属している。日本語の容器（英語でContainer）が語源。実用段階ではないとしながらも、速度・メモリ消費量ともにruncを上回りcrunにわずかに及ばない程度のベンチマーク結果から、ポテンシャルの高さが示されている。

### gVisor

![gVisor](https://res.cloudinary.com/zenn/image/fetch/s--6WCHwQqH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://github.com/google/gvisor/raw/master/g3doc/logo.png?_a=BACAGSGT "gVisor")  
[gVisor](https://gvisor.dev/) は、Googleによって2018年に開始された、Sandbox化したContainerを提供するContainer Runtimeである。runcとcrunがホストKernelを利用してContainerを実行しているのに対し、gVisorがゲストKernelとしてContainerのシステムコールを受け付ける方式をとる。すなわちgVisorは、Containerという仕組みが一つのホストKernelを共有している以上ホストKernelの脆弱性から逃れることはできないと問題視し、ホストKernelとContainerプロセスの間に、システムコールの受付を担うSentry、ファイルシステムの提供を担うGoferというコンポーネントを用いて、proxyレイヤーとなるゲストKernelを形成することでContainerをホストKernelから分離し、セキュリティ性を高め、フットプリントの柔軟性も向上させている（ただし、ゲストKernelが存在する分、動作のオーバーヘッドには注意が必要である）。Containerの実行にはrunscを利用しており、ContainerをOCIに準拠させている [^91] [^92] 。

> ![gVisor Architecture](https://res.cloudinary.com/zenn/image/fetch/s--qzVyEpbS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://gvisor.dev/docs/Sentry-Gofer.png?_a=BACAGSGT "gVisor Architecture")  
> *gVisor Architecture*  
> *引用： [gVisor Documentation](https://gvisor.dev/docs/)*

> **note**  
> コンピュータセキュリティの文脈でのSandboxは、システム障害やソフトウェアの脆弱性の拡散を軽減するために分離されたプロセスを意味する。友達と遊ぶのが苦手な子供に与えた個人のための遊びスペースをSandboxと呼んだことに由来するといわれている。Linux ContainerはホストOSのKernelを共有していることから、Sandboxとは呼べないというのが、gVisorの見方である。  
> 似た思想に [Nabla](https://nabla-containers.github.io/) というContainer Runtimeもある。

### Kata container

![Kata container](https://res.cloudinary.com/zenn/image/fetch/s--O-RGWHKa--/https://www.vectorlogo.zone/logos/katacontainersio/katacontainersio-official.svg?_a=BACAGSGT "Kata container")  
Kata Containerは、OpenStack Foundationが2018年にリリースした、VMのセキュリティ性とContainerの速度および管理性を統合することを目指したContainer Runtimeである。超軽量なVMを作成し、その上でContainerを動作さあせるという方式であり、その分離性故、セキュリティ性が非常に高いと言える。2015年にリリースされたIntelの [Intel Clear Containers](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-clear-containers-1-the-container-landscape.html) と2017年9月にリリースされたHyperの [runV](https://github.com/hyperhq/runv) それぞれの技術を組み合わせて構築されており、現在はOCI準拠のContainer Runtimeである `kata-kontainer` を実装し、プラグインを通じてCRIとも互換性をもたせている。 `kata-runtime` は、各Containerまたは各Podに対してQEMU/KVM（Quick Emulator/Kernel-based Virtual Machine）を作成し、その中で `kata-agent` というdaemonプロセスを実行することで、Containerを管理する [^93] 。

> ![Kata container architecture](https://res.cloudinary.com/zenn/image/fetch/s--mdGCfnvS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://katacontainers.io/static/a43936f549270231f0f81e52b99494f9/43a2d/kata-explained1%25402x.png?_a=BACAGSGT "Kata container architecture")  
> *Kata container architecture*  
> *引用： [Kata Containers](https://katacontainers.io/)*

> **note**  
> Kata containerプロジェクトがアナウンスされたときの参画企業はIntelとHyperの他に、  
> 99cloud, AWcloud, Canonical, China Mobile, City Network, CoreOS, Dell/EMC, EasyStack, Fiberhome, Google, Huawei, JD.com, Mirantis, NetApp, Red Hat, SUSE, Tencent, Ucloud, UnitedStack, ZTE  
> である。 [^94]

### Inclavare Containers

![Inclavare Containers](https://res.cloudinary.com/zenn/image/fetch/s--crPBNvYJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://inclavare-containers.io/img/logo.png?_a=BACAGSGT)  
[Inclavare Containers](https://inclavare-containers.io/) は、Alibaba社が2020年5月にオープンソース化したContainer runtimeである。データの保護をハードウェアベースで行うことができるTrusted Execution Environment（TEE）と呼ばれる環境を利用して行うConfidential Computing [^95] という方向性を明確に掲げており、2021年9月には最初のConfidential Computing関連のプロジェクトとしてCNCFのSandboxレベルに認定された [^96] 。Confidential Computingは、データの保存中や転送中だけでなく、使用中も暗号化されたままにできるため、高い機密性を維持しながらデータを取り扱うことができる点で、非常に高いポテンシャルを示している [^97] 。その一方で、SDKを利用した環境構築が非常に難易度が高く自前で用意することが難しいこと、単一のベア前たるアーキテクチャに基づいて実装されるためクラウドサービスへの導入の敷居が高く、クラウドプロバイダーに用意してもらうことが難しいなどの理由で、IaaSレイヤーで実装する試みはほぼ失敗していた。そこでAlibaba社が、ContainerエコシステムにConfidential Computingを導入しようと開始したのが、このInclavare Containersというプロジェクトである [^98] 。  
Inclavare Containersは、runeという低レベルのContainer Runtimeで、Enclave Containerと呼ばれるIntel SGX（Software Guard Extensions）のEnclaveを利用したContainerを作成する（Intel SGXはTEEの一つであり、それにより暗号化された一部のメモリがEnclaveである [^99] ）。runeはOCIに準拠し、runeのバックエンドとして動作するenclave-runtimeというコンポーネントが、Enclave内でアプリケーションを管理するという形をとる。

> **note**  
> 現在主流のTEEは、下記の3つである。
> 
> - [Intel SGX](https://www.intel.com/content/www/us/en/developer/tools/software-guard-extensions/overview.html)
> - [ARM TrustZone](https://www.arm.com/technologies/trustzone-for-cortex-a)
> - [AMD SEV](https://www.amd.com/en/processors/amd-secure-encrypted-virtualization)

> ![Inclave Containers Architecture](https://res.cloudinary.com/zenn/image/fetch/s--vbCVPmN6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://inclavare-containers.io/img/home/Architecture1.jpg?_a=BACAGSGT)  
> *Inclave Containers Architecture*

## 5.3. Container Runtime以外の軽量仮想環境ツール

### Pantavisor

![Pantavisor](https://res.cloudinary.com/zenn/image/fetch/s--nvgw7O6L--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/778d3e19119a3404d0d0c1a2.png%3Fsha%3D4e01ef7acbeea5591b515d24eae4091ff2e79f53)  
[Pantavisor](https://www.pantavisor.io/) は、2021年にPantacor社からリリースされた、IoTデバイス向けの（すなわち、安全かつ迅速にデバイスのアップデートを行えるように遠隔で管理が可能な）組み込みLinuxを構築するフレームワークである [^100] 。軽量LXCで動く独自の組み込みLinuxを作成したりや任意のDocker containerをLXCに変換してContainer化された組み込みシステムブロックを構築・管理するPantavisor Linux、Pantavisor対応デバイスのファームウェア・ソフトウェアのライフサイクルを遠隔管理するPantacor Hub、さらに細かい粒度での管理を可能とするPantacor Fleetの3つのコア要素で構成される [^101] [^102] 。crunと同様にC言語で開発されており、LXCベースでContainerを取り扱うため、低レベルContainer Runtimeとして考えられることもある <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-67">[67:2]</a></sup> 。ファームウェア、OS、BSPをも移植可能なContainer化されたブロックとし、最小フットプリントで実行可能することができるため、よりエッジコンピューティング、組み込み機器でContainerを利用することが意識されたプロジェクトの例として挙げられる。また、その他のContainer Runtimeが必要とするホストOSのレイヤーもContainer化するため、ホストOSのすべての機能を必要としない可能性が高い組み込みデバイスには適している。

> ![Pantavisor Architecture](https://res.cloudinary.com/zenn/image/fetch/s--4CR9RSbV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://i0.wp.com/s33mg.svc.pantacor.com/ph-cms-assets/2021/12/Screenshot-2021-12-10-at-13.01.24.png%3Ffit%3D748%252C830%26ssl%3D1)  
> *Pantavisor Architecture*

### Firecracker

![Firecracker](https://res.cloudinary.com/zenn/image/fetch/s--Nk4Uxr48--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://firecracker-microvm.github.io/img/firecracker-13%403x.png?_a=BACAGSGT)  
[Firecracker](https://firecracker-microvm.github.io/) は、Amazonが2018年にリリースを発表したオープンソースの仮想化技術である。Linux Kernelベースの仮想マシン (KVM) を使用して、Containerのように軽量なmicroVMを作成および管理する仮想マシンモニター (VMM) で、立ち位置はQEMUと同じであるため、Kata ContainerでQEMUの代わりにFirecrackerを使うことができる [^103] 。Kata containerと同様に軽量のVMを走らせ、他のVMとの相互作用しないように制限をするSingle Processモデルで動作させるなどの工夫により、Containerよりもシステムの隔離度を高めてセキュアな環境を構築する [^104] 。またFirecrackerは、Rustで記述されたオープンソースのVMMであるcrosvm（Chromium OSのVMM）のフォークであり、AWS Fargate、AWS Lambdaのバックエンドで利用されている [^105] 。  
[firecracker-containerd](https://github.com/firecracker-microvm/firecracker-containerd) を利用することで、containerdを使用していわゆるContainerと同様に軽量にFirecrackerのmicroVMを管理することができることに加え、KVMハイパーバイザーを介して分離レイヤーを追加することもできる <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-104">[104:1]</a></sup> [^106] 。

> ![Firecracker architecture](https://res.cloudinary.com/zenn/image/fetch/s--8a-NZFZr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://firecracker-microvm.github.io/img/diagram-desktop%403x.png?_a=BACAGSGT)  
> *Firecracker architecture*

> **note**  
> 2014年ごろから、AmazonはサーバーレスのサービスであるAWS Lamdaを構築する際、需要に応じてリソースを柔軟に変更可能とするため、VMまたはContainerの利用を検討したが、システムを隔離することによるセキュリティ性向上を狙い、VMを採用した。しかし従来のVMでは、ユーザーが求める実行速度に満たなかったため、Firecrackerの開発に至ったという経緯がある [^107] 。

> **note**  
> FirecrackerがContainer Runtimeではない件に関しては、下記のリンクをご参考まで
> 
> - [Firecracker はコンテナランタイムではありません](https://blog.8-p.info/ja/2020/12/27/fc-and-fccd/)
> - [Kazuyoshi Kato様のコメント](https://zenn.dev/link/comments/13267c773d6ba0)

### Unikraft

![Unikraft](https://res.cloudinary.com/zenn/image/fetch/s--7QPE8kUC--/https://unikraft.org/assets/imgs/unikraft.svg?_a=BACAGSGT)  
[Unikraft](https://unikraft.org/) は、2017年にNEC Laboratories Europeプロジェクトとして開発が開始された、Unikernelと呼ばれる仮想環境を構築するフレームワークである <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-96">[96:1]</a></sup> <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-95">[95:1]</a></sup> 。2021年にUnikraft社として設立した。  
Unikernelは、実行したいサービスに必要最低限の機能のみを持たせたKernelである。これをHypervisorで動かすことで、短時間起動、低メモリフットプリント、高ネットワークスループットの非常に軽量な仮想環境を得ることができる。Containerが軽量だがセキュリティ性に不安があり、Hypervisorを用いたVMはセキュアだが軽量間に欠けるという状況の中、Unikernelは前述のような高機能・軽量性に加えて、Kernelが最小限で攻撃対象領域が少ないためセキュリティ性が高いともいえるため、ContainerとVMのいいとこどりができるとして期待できる。しかし、大きなデメリットとして、Unikernelは基本的に手動で構築する必要があったことだった（ [MiniOS](https://wiki.xenproject.org/wiki/Mini-OS) 、 [OSv](https://osv.io/) など） <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-98">[98:1]</a></sup> 。  
Unikraftは、"Everything is a library"というコンセプトのもと、OSの機能をlibraryに分けて、必要なコンポーネントを選びやすくすることでUnikernelの構築および最適化を簡単にすることを目指している。Unikraftはいまだメジャーリリースはされていないが、DockerやそのほかのUnikernel構築フレームワークと比べて高いパフォーマンスを示している <sup><a href="https://zenn.dev/ttnt_1013/articles/#fn-7c92-99">[99:1]</a></sup> 。さらに、前述のIntel SGXと組み合わせてさらに隔離度を向上させる試みも行われている [^108] 。

> ![VM vs Unikernel](https://res.cloudinary.com/zenn/image/fetch/s--gNDTN5go--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/1919789fcbc4947295923867.png%3Fsha%3D0ec286c0deed6ca76aaafe6178650a04137dc89f)  
> *VM vs Unikernel*

> ![Unikraft Architecture](https://res.cloudinary.com/zenn/image/fetch/s--Zp2DyLiZ--/https://unikraft.org/assets/imgs/unikraft-architecture.svg?_a=BACAGSGT)  
> *Unikraft Architecture*

### WasmEdge

![WasmEdge](https://res.cloudinary.com/zenn/image/fetch/s--6ymQiLl---/https://landscape.cncf.io/logos/wasm-edge-runtime.svg?_a=BACAGSGT)  
[WasmEdge](https://wasmedge.org/) は、軽量で高性能な [WebAssembly（Wasm）](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/2093/) を実行できるVMで、2021年にCNCFのSandboxプロジェクトとして認定されている。  
2019年に台北の [Second State](https://www.secondstate.io/) が、SSVM（Second State Virtual Machine）という [Wasm](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/2093/) 互換のRuntimeをリリースした。 [Wasm](https://lethediana.sakura.ne.jp/tech/archives/summary-ja/2093/) はブラウザ内（クライアント側）でプログラムを高速で動かす実行環境であり、様々なプログラミング言語をサポートし、Containerよりも軽量かつ高速に動作する。当初、SSVMはサーバー側でWasmに互換性を持たせることに焦点が置かれていたが [^109] 、2021年5月にエッジや分散処理用途も視野に入れてWasmEdgeにプロジェクト名を変更した [^110] 。  
Docker社は、2022年のアナウンスでWasmをLinux Containerを補完するテクノロジーであるとし [^111] 、Docker DesktopにWasmEdgeを用いてWasmアプリケーションを実行することができる環境を実装、Linux ContainerのようにWasmアプリケーションを実行できるようになっている（Wasm Containerと呼ばれる） [^112] 。

> ![Docker+Wasm Architecture](https://res.cloudinary.com/zenn/image/fetch/s--kqrM_ZPH--/https://www.docker.com/wp-content/uploads/2022/10/docker-containerd-wasm-diagram.png.webp?_a=BACAGSGT)  
> *Docker+Wasm Architecture*

## 6\. おわりに

Containerの利用範囲はWebサービスを中心に拡大を続け、ついにはIoT用途やエッジコンピューティングにまで届きつつある。それによってContainerに対して期待される要件が多種多様となり、さまざまなContainerやOrchestrationツールが登場している。したがって、適切な環境でContainerを扱うためには、本記事でみてきたような状況や背景の把握をしたうえで、今後の動向をキャッチアップしていくことが非常に重要である。

## 参考

脚注

[GitHubで編集を提案](https://github.com/wgb-256/zenn-content/blob/master/articles/f36e251a0cd24e.md)

1470

58

この記事に贈られたバッジ

![参考になった](https://static.zenn.studio/images/badges/paid/badge-frame-10.svg) ![Thank you](https://static.zenn.studio/images/badges/paid/badge-frame-5.svg) ![Thank you](https://static.zenn.studio/images/badges/paid/badge-frame-3.svg)

1470

58

[^1]: [Docker architecture](https://docs.docker.com/get-started/overview/#docker-architecture)

[^2]: [dockerd](https://docs.docker.com/engine/reference/commandline/dockerd/)

[^3]: [Implementation Levels of Virtualization](https://www.brainkart.com/article/Implementation-Levels-of-Virtualization_11328/)

[^4]: [Docker: It’s not dead yet, but there’s a tendency to walk away, security report finds](https://devclass.com/2021/01/13/sysdig-container-security-and-usage-report-2021/)

[^5]: [What We Announced Today and Why it Matters](https://www.mirantis.com/blog/mirantis-acquires-docker-enterprise-platform-business/)

[^6]: [Docker Now Requiring Paid Subscription for Large Businesses](https://www.infoq.com/news/2021/09/docker-desktop-subscriptions/)

[^7]: [Pricing and Subscriptions](https://www.docker.com/pricing/)

[^8]: [The Top 5 Docker Security Threats You Need To Know About 2023](https://rsk-cyber-security.com/security/the-top-5-docker-security-threats-you-need-to-know-about-2023/)

[^9]: [Docker malware is now common, so devs need to take Docker security seriously](https://www.zdnet.com/article/docker-malware-is-now-common-so-devs-need-to-take-docker-security-seriously/#ftag=RSSbaffb68)

[^10]: [Run the Docker daemon as a non-root user (Rootless mode)](https://docs.docker.com/engine/security/rootless/)

[^11]: [Will Docker’s Lacklustre Security Lead to its Untimely Demise?](https://analyticsindiamag.com/will-dockers-lacklustre-security-lead-to-its-untimely-demise/)

[^12]: [Docker Alternatives for Containerization & Their Standout Features](https://www.simplilearn.com/docker-alternatives-article)

[^13]: [What Does Kubernetes’ Docker Deprecation Mean for Users](https://www.knowledgehut.com/blog/devops/kubernetes-docker-deprecation)

[^14]: [chroot in *Wikipedia*](https://en.wikipedia.org/wiki/Chroot)

[^15]: [Linux Virtualization – Chroot Jail](https://www.geeksforgeeks.org/linux-virtualization-using-chroot-jail/)

[^16]: [FreeBSD documents Chapter 16. Jails](https://docs.freebsd.org/en/books/handbook/jails/)

[^17]: [Linux-VServer in *Wikipedia*](https://en.wikipedia.org/wiki/Linux-VServer)

[^18]: [Process containers](https://lwn.net/Articles/236038/)

[^19]: [cgroups7 — Linux manual page](https://man7.org/linux/man-pages/man7/cgroups.7.html)

[^20]: [Warden](https://docs.huihoo.com/cloudfoundry/documentation/concepts/architecture/warden.html)

[^21]: 

[^22]: [google/lmctfy](https://github.com/google/lmctfy)

[^23]: [What is the difference between lmctfy and lxc](https://stackoverflow.com/questions/19196495/what-is-the-difference-between-lmctfy-and-lxc)

[^24]: [Kubernetes: A Brief History of Orchestration & Container Management](https://www.metarouter.io/blog-posts/kubernetes-a-brief-history-of-orchestration-container-management)

[^25]: [DotCloud Pivots And Wins Big With Docker, The Cloud Service Now Part Of Red Hat OpenShift](https://techcrunch.com/2013/09/19/dotcloud-pivots-and-wins-big-with-docker-the-cloud-service-now-part-of-red-hat-openshift/)

[^26]: [How Docker Was Born](https://stackshare.io/posts/how-docker-was-born)

[^27]: [Docker Desktop 0.9: Introducing Execution Drivers and libcontainer](https://www.docker.com/blog/docker-0-9-introducing-execution-drivers-and-libcontainer/)

[^28]: [Evolution of Docker from Linux Containers](https://www.baeldung.com/linux/docker-containers-evolution)

[^29]: [［速報］Google Container Engine発表。Dockerコンテナを実行しKubernetesで管理するクラウドサービス](http://www.publickey1.jp/blog/14/google_container_enginedockerkubernetes.html)

[^30]: [［速報］Dockerをサポートした「Amazon EC2 Container Service」発表。AWS re:Invent 2014](https://www.publickey1.jp/blog/14/dockeramazon_ec2_container_serviceaws_reinvent_2014.html)

[^31]: 

[^32]: [Container Linux in *Wikipedia*](https://en.wikipedia.org/wiki/Container_Linux)

[^33]: [LXC and LXD: a different container story](https://lwn.net/Articles/907613/)

[^34]: [LXD 0.1 リリースのお知らせ](https://linuxcontainers.org/ja/lxd/news/2015_02_13_00_00.html)

[^35]: [What Has the Open Container Initiative Achieved in Its First Year?](https://www.linux.com/news/what-has-open-container-initiative-achieved-its-first-year/)

[^36]: [Container Runtimes Part 1: An Introduction to Container Runtimes](https://www.ianlewis.org/en/container-runtimes-part-1-introduction-container-r)

[^37]: [A history of low-level Linux container runtimes](https://opensource.com/article/18/1/history-low-level-container-runtimes)

[^38]: [Yet Another Brief History of container(d)](https://erzeghi.medium.com/yet-another-brief-history-of-container-d-2962eac9679e)

[^39]: [Introducing runC: a lightweight universal container runtime](https://www.docker.com/blog/runc/)

[^40]: 

[^41]: [The History of Kubernetes on a Timeline](https://blog.risingstack.com/the-history-of-kubernetes/)

[^42]: [Everything you wanted to know about Kubernetes but were afraid to ask](https://cloudplatform.googleblog.com/2015/01/everything-you-wanted-to-know-about-Kubernetes-but-were-afraid-to-ask.html)

[^43]: [Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center](https://people.csail.mit.edu/matei/papers/2011/nsdi_mesos.pdf)

[^44]: [Apache Mesos in *Wikipedia*](https://en.wikipedia.org/wiki/Apache_Mesos)

[^45]: [Why We Chose Kubernetes Over Mesos (DC/OS)](https://logz.io/blog/kubernetes-vs-mesos/)

[^46]: [How Did Kubernetes Win the Container Orchestration War?](https://hackernoon.com/how-did-kubernetes-win-the-container-orchestration-war-lp1l3x01)

[^47]: [CRI: the Container Runtime Interface](https://github.com/kubernetes/kubernetes/blob/242a97307b34076d5d8f5bbeb154fa4d97c9ef1d/docs/devel/container-runtime-interface.md)

[^48]: [Running production applications in containers: Introducing OCID](https://www.redhat.com/en/blog/running-production-applications-containers-introducing-ocid)

[^49]: [Introducing CRI-O 1.0](https://www.redhat.com/en/blog/introducing-cri-o-10)

[^50]: [Comparing Container Runtimes: containerd vs. Docker](https://earthly.dev/blog/containerd-vs-docker/)

[^51]: [Cloud Native Computing Foundationがcontainerdの卒業を発表](https://prtimes.jp/main/html/rd/p/000000008.000042042.html)

[^52]: [Amazon Elastic Container Service for Kubernetes](https://aws.amazon.com/jp/blogs/news/amazon-elastic-container-service-for-kubernetes/)

[^53]: [Google Kubernetes Engine 1.10 is generally available and ready for the enterprise](https://cloud.google.com/blog/products/gcp/google-kubernetes-engine-1-10-is-generally-available-and-ready-for-the-enterprise/)

[^54]: [Introducing Moby Project: a new open-source project to advance the software containerization movement](https://www.docker.com/blog/introducing-the-moby-project/)

[^55]: [Dockerが「Moby Project」を発表。すべてをコンテナで組み立てる世界を目指す。DockerCon 2017](https://www.publickey1.jp/blog/17/dockermoby_projectdockercon_2017.html)

[^56]: [Moby Project Roadmap](https://github.com/moby/moby/blob/master/ROADMAP.md)

[^57]: [Why Containers and WebAssembly Work Well Together](https://www.docker.com/blog/why-containers-and-webassembly-work-well-together/)

[^58]: [WebAssembly and Containers](https://www.youtube.com/watch?v=OGcm3rHg630)

[^59]: [Tweet by @solomonstre in Mar 28, 2019](https://twitter.com/solomonstre/status/1111004913222324225?lang=en)

[^60]: [Introducing the Docker+Wasm Technical Preview](https://www.docker.com/blog/docker-wasm-technical-preview/)

[^61]: [Docker+Wasm Integration #426](https://github.com/docker/roadmap/issues/426)

[^62]: [Kubernetes 1.7: Security Hardening, Stateful Application Updates and Extensibility](https://kubernetes.io/blog/2017/06/kubernetes-1-7-security-hardening-stateful-application-extensibility-updates/)

[^63]: [Introducing Operators: Putting Operational Knowledge into Software](https://web.archive.org/web/20170129131616/https://coreos.com/blog/introducing-operators.html)

[^64]: [What is an Operator](https://operatorhub.io/what-is-an-operator)

[^65]: [Microsoft to acquire Deis to help companies innovate with containers](https://blogs.microsoft.com/blog/2017/04/10/microsoft-acquire-deis-help-companies-innovate-containers/)

[^66]: [Helm 3 Preview: Charting Our Future – Part 1: A History of Helm](https://helm.sh/blog/helm-3-preview-pt1/)

[^67]: [Cloud-Native Workload Orchestration at the Edge: A Deployment Review and Future Directions](https://www.mdpi.com/1424-8220/23/4/2215)

[^68]: [Introducing k3s: The Lightweight Kubernetes Distribution Built for the Edge](https://www.suse.com/c/rancher_blog/introducing-k3s-the-lightweight-kubernetes-distribution-built-for-the-edge/)

[^69]: [TOC Approves KubeEdge as Incubating Project](https://www.cncf.io/blog/2020/09/16/toc-approves-kubeedge-as-incubating-project/)

[^70]: [NVIDIA GPU Operator: Simplifying GPU Management in Kubernetes](https://developer.nvidia.com/blog/nvidia-gpu-operator-simplifying-gpu-management-in-kubernetes/)

[^71]: [The Xilinx device plugin for Kubernetes](https://xilinx.github.io/video-sdk/v1.5/deploying_with_kubernetes.html)

[^72]: [Intel FPGA device plugin for Kubernetes](https://intel.github.io/intel-device-plugins-for-kubernetes/cmd/fpga_plugin/README.html)

[^73]: [Unified balenaOS releases are now available](https://blog.balena.io/unified-balenaos-releases-now-available/)

[^74]: [EVE Kubernetes Control Plane Integration - Draft](https://wiki.lfedge.org/display/EVE/EVE+Kubernetes+Control+Plane+Integration+-+Draft)

[^75]: [Docker 1.11: The first runtime built on containerd and based on OCI technology](https://www.docker.com/blog/docker-engine-1-11-runc/)

[^76]: [Sysdig 2022 Cloud-Native Security and Usage Report](https://sysdig.com/2022-cloud-native-security-and-usage-report/)

[^77]: [Chapter 1. Using the CRI-O Container Engine](https://access.redhat.com/documentation/en-us/openshift_container_platform/3.11/html/cri-o_runtime/use-crio-engine)

[^78]: [Introducing CRI-O 1.0](https://www.redhat.com/ja/blog/introducing-cri-o-10)

[^79]: [Interactions between cri-o and conmon in Kubernetes](https://insujang.github.io/2019-11-18/interactions-between-crio-and-conmon/)

[^80]: [Podman - The next generation of Linux container tools](https://developers.redhat.com/articles/podman-next-generation-linux-container-tools)

[^81]: [Tweet by @orimanabu in Mar 16, 2023](https://twitter.com/orimanabu/status/1636362231054213120)

[^82]: [Manabub Ori様より情報提供いただきました](https://zenn.dev/link/comments/00c35e970efb11)

[^83]: [What is Podman?](https://docs.podman.io/en/latest/)

[^84]: [Podman vs Docker](https://community.cncf.io/events/details/cncf-islamabad-presents-understanding-the-podman-internals/)

[^85]: [Say "Hello" to Buildah, Podman, and Skopeo](https://www.redhat.com/en/blog/say-hello-buildah-podman-and-skopeo)

[^86]: [Introducing runC: a lightweight universal container runtime](https://www.docker.com/blog/runc/)

[^87]: [An introduction to crun, a fast and low-memory footprint container runtime](https://www.redhat.com/sysadmin/introduction-crun)

[^88]: [Documentation / OpenShift Container Platform: Understanding Containers](https://docs.openshift.com/container-platform/4.12/nodes/containers/nodes-containers-using.html)

[^89]: [Tweet by @utam0k in Mar 27, 2021](https://twitter.com/utam0k/status/1375768425889325057)

[^90]: [「あれ、コンテナって何だっけ？」から生まれた Rust で書かれた コンテナランタイム youkiの話 2021-8-28 A-1](https://www.youtube.com/watch?v=YRlzYpbj4I0&t=50s)

[^91]: [What is gVisor?](https://gvisor.dev/docs/)

[^92]: [Getting started with gVisor support in Falco](https://www.cncf.io/blog/2022/09/27/getting-started-with-gvisor-support-in-falco/)

[^93]: [Kata Containers Architecture](https://github.com/kata-containers/documentation/blob/master/design/architecture.md)

[^94]: [Kata Containers Project Launches to Build Secure Container infrastructure](https://www.openstack.org/news/view/365/kata-containers-project-launches-to-build-secure-container-infrastructure#:~:text=Kata%20Containers%20is%20a%20container,the%20home%20of%20open%20infrastructure.)

[^95]: [FOSDEM 2018 Unleashing the Power of Unikernels with Unikraft](https://archive.fosdem.org/2018/schedule/event/vai_power_of_unikernels/attachments/slides/2642/export/events/attachments/vai_power_of_unikernels/slides/2642/unikraft_fosdem.pdf)

[^96]: [Unikraft, a NEC Laboratories Europe spin-off, raises European and U.S. venture capital and begins operation as an independent company](https://uk.nec.com/en_GB/press/PR/20230323233218_4189.html)

[^97]: [Unikraft: Shaping the Future of Cloud Deployments with Unikernels](https://www.future-of-computing.com/unikraft-shaping-the-future-of-cloud-deployments-with-unikernels/)

[^98]: [Unikraft](http://cnp.neclab.eu/projects/unikraft/)

[^99]: [Unikraft Performance](https://unikraft.org/docs/features/performance/)

[^100]: [What is Pantavisor?](https://docs.pantahub.com/#what-is-pantavisor)

[^101]: [A platform for next generation IoT applications](https://pantacor.com/datasheet/)

[^102]: [Pantavisor datasheet](https://s33mg.svc.pantahub.com/ph-cms-assets/2021/10/pantacor_datasheet_2021_02_051021.pdf)

[^103]: [Welcome To The Container Jungle: Docker vs. containerd vs. Nabla vs. Kata vs. Firecracker and more!](https://www.inovex.de/de/blog/containers-docker-containerd-nabla-kata-firecracker/)

[^104]: [Deep Dive into firecracker-containerd](https://www.youtube.com/watch?v=0wEiizErKZw)

[^105]: [AWS Release “Firecracker”, an Open Source Rust-Based microVM for Container and Serverless Workloads](https://www.infoq.com/news/2018/12/aws-firecracker/)

[^106]: [Slides: Deep Dive into firecracker-containerd](https://speakerdeck.com/samuelkarp/deep-dive-into-firecracker-containerd-re-invent-2019-con408)

[^107]: [How AWS’s Firecracker virtual machines work](https://www.amazon.science/blog/how-awss-firecracker-virtual-machines-work)

[^108]: [Improving security and isolation of Unikraft with Intel SGX](https://unikraft.org/blog/2022-07-05-unikraft-gsoc-intel-sgx/)

[^109]: [Second State releases WebAssembly for the server side](https://medium.com/wasm/second-state-releases-webassembly-for-the-server-side-7e9187d2968f)

[^110]: 

[^111]: [Introducing the Docker+Wasm Technical Preview](https://www.docker.com/blog/docker-wasm-technical-preview/)

[^112]: [WebAssembly: Docker without containers!](https://wasmlabs.dev/articles/docker-without-containers/)