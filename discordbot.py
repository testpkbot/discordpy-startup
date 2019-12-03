from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
    
@bot.command(name="ゴリランダー")
async def goriranda(ctx):
    await ctx.send(f"H:100 A:125 B:90 C:60 D:70 S:85")
    
@bot.command(name="エースバーン")
async def esuban(ctx):
    await ctx.send(f"H:80 A:116 B:75 C:65 D:75 S:119")

    
@bot.command(name="インテレオン")
async def intereon(ctx):
    await ctx.send(f"H:70 A:85 B:65 C:125 D:65 S:120")
    
@bot.command(name="イオルブ")
async def iorubu(ctx):
    await ctx.send(f"H:60 A:45 B:110 C:80 D:120 S:90")    

@bot.command(name="バタフリー")
async def batafuri(ctx):
    await ctx.send(f"H:60 A:45 B:50 C:90 D:80 S:70")
    
@bot.command(name="クワガノン")
async def kuwaganon(ctx):
    await ctx.send(f"H:77 A:70 B:90 C:145 D:75 S:43")    

@bot.command(name="ヨルノズク")
async def yorunozuku(ctx):
    await ctx.send(f"H:100 A:50 B:50 C:86 D:96 S:70")    

@bot.command(name="アーマーガア")
async def amagaa(ctx):
    await ctx.send(f"H:98 A:87 B:105 C:53 D:85 S:67")    

@bot.command(name="ヨクバリス")
async def yokubarisu(ctx):
    await ctx.send(f"H:120 A:95 B:95 C:55 D:75 S:20")    

@bot.command(name="ケンホロウ")
async def kennhorou(ctx):
    await ctx.send(f"H:80 A:115 B:80 C:65 D:55 S:93")    

@bot.command(name="フォックスライ")
async def fokkusurai(ctx):
    await ctx.send(f"H:70 A:58 B:58 C:78 D:92 S:90")    

@bot.command(name="タチフサグマ")
async def tatifusaguma(ctx):
    await ctx.send(f"H:93 A:90 B:101 C:60 D:81 S:95")    

@bot.command(name="バイウールー")
async def baiuru(ctx):
    await ctx.send(f"H:72 A:80 B:100 C:60 D:90 S:88")    

@bot.command(name="ルンパッパ")
async def runpappa(ctx):
    await ctx.send(f"H:80 A:70 B:70 C:90 D:100 S:70")    

@bot.command(name="ダーテング")
async def datengu(ctx):
    await ctx.send(f"H:90 A:100 B:60 C:90 D:60 S:80")    

@bot.command(name="カジリガメ")
async def kajirigame(ctx):
    await ctx.send(f"H:90 A:115 B:90 C:48 D:68 S:74")    

@bot.command(name="レパルダス")
async def reparudasu(ctx):
    await ctx.send(f"H:64 A:88 B:50 C:88 D:50 S:106")    

@bot.command(name="パルスワン")
async def parusuwan(ctx):
    await ctx.send(f"H:69 A:90 B:60 C:90 D:60 S:121")    

@bot.command(name="ホルード")
async def horudo(ctx):
    await ctx.send(f"H:85 A:56 B:77 C:50 D:77 S:78")    

@bot.command(name="チラチーノ")
async def tiratino(ctx):
    await ctx.send(f"H:75 A:95 B:60 C:65 D:60 S:115")    

@bot.command(name="アマージョ")
async def amajo(ctx):
    await ctx.send(f"H:72 A:120 B:98 C:50 D:98 S:72")    

@bot.command(name="ラフレシア")
async def rahuresia(ctx):
    await ctx.send(f"H:75 A:80 B:85 C:110 D:90 S:50")    

@bot.command(name="キレイハナ")
async def kireihana(ctx):
    await ctx.send(f"H:75 A:80 B:95 C:90 D:100 S:50")    

@bot.command(name="ロズレイド")
async def rozureido(ctx):
    await ctx.send(f"H:60 A:70 B:65 C:125 D:105 S:90")    

@bot.command(name="ぺリッパー")
async def perippa(ctx):
    await ctx.send(f"H:60 A:50 B:100 C:95 D:70 S:65")    

@bot.command(name="デンチュラ")
async def dentyura(ctx):
    await ctx.send(f"H:70 A:77 B:60 C:97 D:60 S:108")    

@bot.command(name="ライボルト")
async def raiboruto(ctx):
    await ctx.send(f"H:70 A:75 B:60 C:105 D:60 S:105")    

@bot.command(name="キュウコン")
async def kyuukon(ctx):
        await ctx.send(f"H:73 A:76 B:75 C:81 D:100 S:100")    

@bot.command(name="ウインディ")
async def uindexi(ctx):
    await ctx.send(f"H:90 A:110 B:80 C:100 D:80 S:95")    

@bot.command(name="バイバニラ")
async def baibanira(ctx):
    await ctx.send(f"H:71 A:95 B:85 C:110 D:95 S:79")    

@bot.command(name="マンムー")
async def manmu(ctx):
    await ctx.send(f"H:110 A:130 B:80 C:70 D:60 S:80")    

@bot.command(name="デリバード")
async def deribado(ctx):
    await ctx.send(f"H:45 A:55 B:45 C:65 D:45 S:75")    

@bot.command(name="オニゴーリ")
async def onigori(ctx):
    await ctx.send(f"H:80 A:80 B:80 C:80 D:80 S:80")    

@bot.command(name="ユキメノコ")
async def yukimenoko(ctx):
    await ctx.send(f"H:70 A:80 B:70 C:80 D:70 S:110")    

@bot.command(name="ネンドール")
async def nendoru(ctx):
    await ctx.send(f"H:60 A:70 B:105 C:70 D:120 S:75")    

@bot.command(name="バンバドロ")
async def banbadoro(ctx):
    await ctx.send(f"H:100 A:125 B:100 C:55 D:85 S:35")    

@bot.command(name="イワパレス")
async def iwaparesu(ctx):
    await ctx.send(f"H:70 A:105 B:125 C:65 D:75 S:45")    

@bot.command(name="ゴルーグ")
async def gorugu(ctx):
    await ctx.send(f"H:89 124 B:80 C:55 D:80 S:55")    

@bot.command(name="ムシャーナ")
async def musyana(ctx):
    await ctx.send(f"H:116 A:55 B:85 C:107 D:95 S:29")    

@bot.command(name="ネイティオ")
async def neitexio(ctx):
    await ctx.send(f"H:65 A:75 B:70 C:95 D:70 S:95")    

@bot.command(name="キテルグマ")
async def kiteruguma(ctx):
    await ctx.send(f"H:120 A:125 B:80 C:55 D:60 S:60")    

@bot.command(name="ユキノオー")
async def yukinoo(ctx):
    await ctx.send(f"H:90 A:92 B:75 C:92 D:85 S:60")    

@bot.command(name="キングラー")
async def kingura(ctx):
    await ctx.send(f"H:55 A:130 B:115 C:50 D:50 S:75")    

@bot.command(name="ヌオー")
async def nuo(ctx):
    await ctx.send(f"H:95 A:85 B:85 C:65 D:65 S:35")    

@bot.command(name="シザリガー")
async def sizariga(ctx):
    await ctx.send(f"H:63 A:120 B:85 C:90 D:55 S:55")    

@bot.command(name="テッカニン")
async def tekkanin(ctx):
    await ctx.send(f"H:61 A:90 B:45 C:50 D:50 S:160")    

@bot.command(name="ヌケニン")
async def nukenin(ctx):
    await ctx.send(f"H:1 A:90 B:45 C:30 D:30 S:40")    

@bot.command(name="サワムラー")
async def sawamura(ctx):
    await ctx.send(f"H:50 A:120 B:53 C:35 D:110 S:87")    

@bot.command(name="エビワラー")
async def ebiwara(ctx):
    await ctx.send(f"H:50 A:105 B:79 C:35 D:110 S:76")    

@bot.command(name="カポエラー")
async def kapoera(ctx):
    await ctx.send(f"H:50 A:95 B:95 C:35 D:110 S:70")    

@bot.command(name="ゴロンダ")
async def goronda(ctx):
    await ctx.send(f"H:95 A:124 B:78 C:69 D:71 S:58")    

@bot.command(name="ギギギアル")
async def gigigiaru(ctx):
    await ctx.send(f"H:60 A:100 B:115 C:70 D:85 S:90")    

@bot.command(name="ビークイン")
async def bikuin(ctx):
    await ctx.send(f"H:70 A:80 B:102 C:80 D:102 S:40")    

@bot.command(name="ドータクン")
async def dotakun(ctx):
    await ctx.send(f"H:67 A:89 B:116 C:79 D:116 S:33")    

@bot.command(name="サーナイト")
async def sanaito(ctx):
    await ctx.send(f"H:68 A:65 B:65 C:125 D:115 S:80")    

@bot.command(name="エルレイド")
async def erureido(ctx):
    await ctx.send(f"H:68 A:125 B:65 C:65 D:115 S:80")    

@bot.command(name="フワライド")
async def huwaraido(ctx):
    await ctx.send(f"H:150 A:80 B:44 C:90 D:54 S:80")    

@bot.command(name="ワタシラガ")
async def watasiraga(ctx):
    await ctx.send(f"H:60 A:50 B:90 C:80 D:120 S:60")    

@bot.command(name="チェリム")
async def tixerimu(ctx):
    await ctx.send(f"H:70 A:60 B:70 C:87 D:78 S:85")    

@bot.command(name="スカタンク")
async def sukatanku(ctx):
    await ctx.send(f"H:103 A:93 B:67 C:71 D:61 S:84")    

@bot.command(name="ガマゲロゲ")
async def gamageroge(ctx):
    await ctx.send(f"H:105 A:95 B:75 C:85 D:75 S:74")    

@bot.command(name="ヨノワール")
async def yonowaru(ctx):
    await ctx.send(f"H:45 A:100 B:135 C:65 D:135 S:45")    

@bot.command(name="カイリキー")
async def kairiki(ctx):
    await ctx.send(f"H:90 A:130 B:80 C:65 D:85 S:55")    

@bot.command(name="ゲンガー")
async def genga(ctx):
    await ctx.send(f"H:60 A:65 B:60 C:130 D:75 S:110")    

@bot.command(name="ギャラドス")
async def gyaradosu(ctx):
    await ctx.send(f"H:95 A:125 B:79 C:60 D:100 S:81")    

@bot.command(name="アズマオウ")
async def azumaou(ctx):
    await ctx.send(f"H:80 A:92 B:65 C:65 D:80 S:68")    

@bot.command(name="オクタン")
async def okutan(ctx):
    await ctx.send(f"H:75 A:105 B:75 C:105 D:57 S:45")    

@bot.command(name="パルシェン")
async def parusixen(ctx):
    await ctx.send(f"H:50 A:95 B:180 C:85 D:45 S:70")    

@bot.command(name="ミロカロス")
async def mirokarosu(ctx):
    await ctx.send(f"H:95 A:60 B:79 C:100 D:125 S:81")    

@bot.command(name="バスラオ")
async def basurao(ctx):
    await ctx.send(f"H:70 A:92 B:65 C:80 D:55 S:98")    

@bot.command(name="ヨワシ")
async def yowasi(ctx):
    await ctx.send(f"H:45 A:20 B:20 C:25 D:25 S:40")    

@bot.command(name="ナマコブシ")
async def namakobusi(ctx):
    await ctx.send(f"H:55 A:60 B:130 C:30 D:130 S:5")    

@bot.command(name="ダストダス")
async def dasutodasu(ctx):
    await ctx.send(f"H:80 A:95 B:82 C:60 D:82 S:75")    

@bot.command(name="マルヤクデ")
async def maruyakude(ctx):
    await ctx.send(f"H:100 A:115 B:65 C:90 D:90 S:65")    

@bot.command(name="セキタンザン")
async def sekitanzan(ctx):
    await ctx.send(f"H:110 A:80 B:120 C:80 D:90 S:30")    

@bot.command(name="ダグトリオ")
async def dagutorio(ctx):
    await ctx.send(f"H:35 A:100 B:50 C:50 D:70 S:120")    

@bot.command(name="ドリュウズ")
async def doryuuzu(ctx):
    await ctx.send(f"H:110 A:135 B:60 C:50 D:65 S:88")    

@bot.command(name="ギガイアス")
async def gigaiasu(ctx):
    await ctx.send(f"H:85 A:135 B:130 C:60 D:80 S:25")    

@bot.command(name="ローブシン")
async def robusin(ctx):
    await ctx.send(f"H:105 A:140 B:95 C:55 D:65 S:45")    

@bot.command(name="ココロモリ")
async def kokoromori(ctx):
    await ctx.send(f"H:67 A:57 B:55 C:77 D:55 S:114")    

@bot.command(name="オンバーン")
async def onban(ctx):
    await ctx.send(f"H:85 A:70 B:80 C:97 D:80 S:123")    

@bot.command(name="ハガネール")
async def haganeru(ctx):
    await ctx.send(f"H:75 A:85 B:200 C:55 D:65 S:30")    

@bot.command(name="カマスジョー")
async def kamasujo(ctx):
    await ctx.send(f"H:61 A:123 B:60 C:60 D:50 S:136")    

@bot.command(name="ニャイキング")
async def nyaikingu(ctx):
    await ctx.send(f"H:70 A:110 B:100 C:50 D:60 S:50")    

@bot.command(name="ペルシアン")
async def perusian(ctx):
    await ctx.send(f"H:65 A:70 B:60 C:65 D:65 S:115")    

@bot.command(name="マホイップ")
async def mahoippu(ctx):
    await ctx.send(f"H:65 A:60 B:75 C:110 D:121 S:64")    

@bot.command(name="アブリボン")
async def aburibon(ctx):
    await ctx.send(f"H:60 A:55 B:60 C:95 D:70 S:124")    

@bot.command(name="ナットレイ")
async def nattorei(ctx):
    await ctx.send(f"H:74 A:94 B:131 C:54 D:116 S:20")    

@bot.command(name="パンプジン")
async def panpujin(ctx):
    await ctx.send(f"H:65 A:90 B:122 C:58 D:75 S:84")    

@bot.command(name="ライチュウ")
async def raityuu(ctx):
    await ctx.send(f"H:60 A:90 B:55 C:90 D:80 S:110")    

@bot.command(name="シャワーズ")
async def syawazu(ctx):
    await ctx.send(f"H:130 A:65 B:60 C:110 D:95 S:65")    

@bot.command(name="サンダース")
async def sandasu(ctx):
    await ctx.send(f"H:65 A:65 B:60 C:110 D:95 S:130")    

@bot.command(name="ブースター")
async def busuta(ctx):
    await ctx.send(f"H:65 A:130 B:60 C:95 D:110 S:65")    

@bot.command(name="エーフィ")
async def efi(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ブラッキー")
async def burakki(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="リーフィア")
async def rifia(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="グレイシア")
async def gureisia(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ニンフィア")
async def ninfia(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アップリュー")
async def appuryu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="タルップル")
async def taruppuru(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ニャオニクス")
async def nyaonikusu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ペロリーム")
async def perorimu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="フレフワン")
async def hurehuwan(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オニシズクモ")
async def onisizukumo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ソーナンス")
async def sonansu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ネギガナイト")
async def negiganaito(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ランターン")
async def rantan(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドクロッグ")
async def dokuroggu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ズルズキン")
async def zuruzukin(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マッギョ")
async def maggyo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ツボツボ")
async def tubotubo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナマズン")
async def namazun(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="トリトドン")
async def toritodon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="グソクムシャ")
async def gusokumusya(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ガメノデス")
async def gamenodesu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サニゴーン")
async def sanigon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オーロンゲ")
async def oronge(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ブリムオン")
async def burimuon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エンニュート")
async def ennyuto(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="キリキザン")
async def kirikizan(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナゲキ")
async def nageki(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダゲキ")
async def dageki(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マタドガス")
async def matadogasu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウソッキー")
async def usokki(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ピクシー")
async def pikusi(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="トゲキッス")
async def togekkisu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カビゴン")
async def kabigon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エルフーン")
async def erufun(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドサイドン")
async def dosaidon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ゴチルゼル")
async def gotiruzeru(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ランクルス")
async def rankurusu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シュバルゴ")
async def syubarugo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アギルダー")
async def agiruda(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オーベム")
async def obemu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ツンベアー")
async def tunbea(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウォーグル")
async def uxoguru(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バルジーナ")
async def barujina(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドラピオン")
async def dorapion(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シャンデラ")
async def syandera(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カラマネロ")
async def karamanero(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マニューラ")
async def manyura(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヤミラミ")
async def yamirami(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="クチート")
async def kutito(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マラカッチ")
async def marakatti(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シンボラー")
async def sinbora(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ルカリオ")
async def rukario(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="コータス")
async def kotasu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ミミッキュ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダイオウドウ")
async def daioudou(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ハリーセン")
async def harisen(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ブルンゲル")
async def burungeru(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドヒドイデ")
async def dohidoide(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウッウ")
async def uxtuu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ストリンダー")
async def sutorinda(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サダイジャ")
async def sadaija(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カバルドン")
async def kabarudon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アイアント")
async def aianto(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="クイタラン")
async def kuitaran(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エレザード")
async def erezado(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ルチャブル")
async def rutyaburu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="フライゴン")
async def huraigon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オノノクス")
async def ononokusu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="デスバーン")
async def desuban(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="デスカーン")
async def desukan(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ギルガルド")
async def girugarudo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ギャロップ")
async def gyaroppu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ポットデス")
async def pottodesu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="イエッサン")
async def iessan(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オーロット")
async def orotto(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マシェード")
async def masixedo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヤレユータン")
async def yareyutan(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナゲツケサル")
async def nagetukesaru(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="モルペコ")
async def morupeko(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="タイレーツ")
async def tairetu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ジジーロン")
async def jijiron(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バクガメス")
async def bakugamesu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="トゲデマル")
async def dogedemaru(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="モスノウ")
async def mosunou(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オトスパス")
async def otosupasu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バチンウニ")
async def bantiuni(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マンタイン")
async def mantain(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ホエルオー")
async def hoeruo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="クレベース")
async def kurebesu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダダリン")
async def dadarin(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ラプラス")
async def rapurasu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ルナトーン")
async def runaton(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ソルロック")
async def sorurokku(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バリコオル")
async def barikooru(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヒヒダルマ")
async def hihidaruma(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="イシヘンジン")
async def isihenjin(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="コオリッポ")
async def koorippo(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ジュラルドン")
async def jurarudon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ロトム")
async def rotomu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="パッチラゴン")
async def pattiragon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="パッチルドン")
async def pattirudon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウオノラゴン")
async def uonoragon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウオチルドン")
async def uotirudon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="リザードン")
async def rizadon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シルヴァディ")
async def siruvadexi(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バンギラス")
async def bangirasu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サザンドラ")
async def sazandora(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヌメルゴン")
async def numerugon(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ジャラランガ")
async def jararanga(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドラパルト")
async def doraparuto(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    


@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")

token = os.environ['DISCORD_BOT_TOKEN']
bot.run(token)
