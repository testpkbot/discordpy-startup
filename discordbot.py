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
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")
    
@bot.command(name="エースバーン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")

    
@bot.command(name="インテレオン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")
    
@bot.command(name="イオルブ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バタフリー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")
    
@bot.command(name="クワガノン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヨルノズク")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アーマーガア")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ホシガリス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ケンホロウ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="フォックスライ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="タチフサグマ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バイウールー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ルンパッパ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダーテング")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カジリガメ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="レパルダス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="パルスワン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ホルード")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="チラチーノ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アマージョ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ラフレシア")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="キレイハナ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ロズレイド")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ぺリッパー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="デンチュラ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ライボルト")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="キュウコン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウインディ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バイバニラ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マンムー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="デリバード")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オニゴーリ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ユキメノコ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ネンドール")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バンバドロ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="イワパレス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ゴルーグ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ムシャーナ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ネイティオ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="キテルグマ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ユキノオー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="キングラー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヌオー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シザリガー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="テッカニン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヌケニン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サワムラー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エビワラー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カポエラー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ゴロンダ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ギギギアル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ビークイン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドータクン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サーナイト")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エルレイド")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="フワライド")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ワタシラガ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="チェリム")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="スカタンク")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ガマゲロゲ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヨノワール")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カイリキー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ゲンガー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ギャラドス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アズマオウ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オクタン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="パルシェン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ミロカロス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バスラオ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヨワシ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナマコブシ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダストダス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マルヤクデ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="セキタンザン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダグトリオ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドリュウズ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ギガイアス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ローブシン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ハハコモリ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オンバーン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ハガネール")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カマスジョー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ニャイキング")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ペルシアン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マホイップ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アブリボン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナットレイ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="パンプジン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ライチュウ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シャワーズ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サンダース")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ブースター")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エーフィ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ブラッキー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="リーフィア")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="グレイシア")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ニンフィア")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アップリュー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="タルップル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ニャオニクス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ペロリーム")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="フレフワン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オニシズクモ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ソーナンス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ネギガナイト")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ランターン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドクロッグ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ズルズキン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マッギョ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ツボツボ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナマズン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="トリトドン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="グソクムシャ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ガメノデス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サニゴーン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オーロンゲ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ブリムオン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エンニュート")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="キリキザン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナゲキ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダゲキ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マタドガス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウソッキー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ピクシー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="トゲキッス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カビゴン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エルフーン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドサイドン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ゴチルゼル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ランクルス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シュバルゴ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アギルダー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オーベム")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ツンベアー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウォーグル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バルジーナ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドラピオン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シャンデラ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カラマネロ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マニューラ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヤミラミ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="クチート")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マラカッチ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シンボラー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ルカリオ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="コータス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ミミッキュ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダイオウドウ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ハリーセン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ブルンゲル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドヒドイデ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウッウ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ストリンダー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サダイジャ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="カバルドン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="アイアント")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="クイタラン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="エレザード")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ルチャブル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="フライゴン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オノノクス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="デスバーン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="デスカーン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ギルガルド")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ギャロップ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ポットデス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="イエッサン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オーロット")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マシェード")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヤレユータン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ナゲツケサル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="モルペコ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="タイレーツ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ジジーロン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バクガメス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="トゲデマル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="モスノウ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="オトスパス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バチンウニ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="マンタイン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ホエルオー")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="クレベース")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ダダリン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ラプラス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ルナトーン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ソルロック")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バリコオル")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヒヒダルマ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="イシヘンジン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="コオリッポ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ジュラルドン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ロトム")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="パッチラゴン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="パッチルドン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウオノラゴン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ウオチルドン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="リザードン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="シルヴァディ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="バンギラス")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="サザンドラ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ヌメルゴン")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ジャラランガ")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    

@bot.command(name="ドラパルト")
async def mimikkyu(ctx):
    await ctx.send(f"H:55 A:90 B:80 C:50 D:105 S:96")    


@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")

token = os.environ['DISCORD_BOT_TOKEN']
bot.run(token)
