# -*- coding: utf-8 -*-

'''
Generate randomize rings of kanji with a shared component a la the classic
吾、唯、足るを知る:

　五
矢口隹
　止

Requires cjk-decomp data from
https://cjkdecomp.codeplex.com/wikipage?title=cjk-decomp
to be present in the CWD.
'''

import sys
import random
import re
from codecs import open
from collections import defaultdict

directions = ['top', 'right', 'bottom', 'left']

format = re.compile(r'^(?P<char>[^:]+):(?P<dtype>[^\(]+)'
                    r'\((?P<dchars>[^\)]*)\)\s*$')

decomp = {}

center_chars = defaultdict(lambda: defaultdict(set))

joyo = ('亜哀愛悪握圧扱安暗案以位依偉囲委威尉意慰易為異移維緯胃衣違遺医井域育'
        '一壱逸稲芋印員因姻引飲院陰隠韻右宇羽雨渦浦運雲営影映栄永泳英衛詠鋭液疫'
        '益駅悦謁越閲円園宴延援沿演炎煙猿縁遠鉛塩汚凹央奥往応押横欧殴王翁黄沖億'
        '屋憶乙卸恩温穏音下化仮何価佳加可夏嫁家寡科暇果架歌河火禍稼箇花荷華菓課'
        '貨過蚊我画芽賀雅餓介会解回塊壊快怪悔懐戒拐改械海灰界皆絵開階貝劾外害慨'
        '概涯街該垣嚇各拡格核殻獲確穫覚角較郭閣隔革学岳楽額掛潟割喝括活渇滑褐轄'
        '且株刈乾冠寒刊勘勧巻喚堪完官寛干幹患感慣憾換敢棺款歓汗漢環甘監看管簡緩'
        '缶肝艦観貫還鑑間閑関陥館丸含岸眼岩頑顔願企危喜器基奇寄岐希幾忌揮机旗既'
        '期棋棄機帰気汽祈季紀規記貴起軌輝飢騎鬼偽儀宜戯技擬欺犠疑義議菊吉喫詰却'
        '客脚虐逆丘久休及吸宮弓急救朽求泣球究窮級糾給旧牛去居巨拒拠挙虚許距漁魚'
        '享京供競共凶協叫境峡強恐恭挟教橋況狂狭矯胸脅興郷鏡響驚仰凝暁業局曲極玉'
        '勤均斤琴禁筋緊菌襟謹近金吟銀九句区苦駆具愚虞空偶遇隅屈掘靴繰桑勲君薫訓'
        '群軍郡係傾刑兄啓型契形径恵慶憩掲携敬景渓系経継茎蛍計警軽鶏芸迎鯨劇撃激'
        '傑欠決潔穴結血月件倹健兼券剣圏堅嫌建憲懸検権犬献研絹県肩見謙賢軒遣険顕'
        '験元原厳幻弦減源玄現言限個古呼固孤己庫弧戸故枯湖誇雇顧鼓五互午呉娯後御'
        '悟碁語誤護交侯候光公功効厚口向后坑好孔孝工巧幸広康恒慌抗拘控攻更校構江'
        '洪港溝甲皇硬稿紅絞綱耕考肯航荒行衡講貢購郊酵鉱鋼降項香高剛号合拷豪克刻'
        '告国穀酷黒獄腰骨込今困墾婚恨懇昆根混紺魂佐唆左差査砂詐鎖座債催再最妻宰'
        '彩才採栽歳済災砕祭斎細菜裁載際剤在材罪財坂咲崎作削搾昨策索錯桜冊刷察撮'
        '擦札殺雑皿三傘参山惨散桟産算蚕賛酸暫残仕伺使刺司史嗣四士始姉姿子市師志'
        '思指支施旨枝止死氏祉私糸紙紫肢脂至視詞詩試誌諮資賜雌飼歯事似侍児字寺慈'
        '持時次滋治璽磁示耳自辞式識軸七執失室湿漆疾質実芝舎写射捨赦斜煮社者謝車'
        '遮蛇邪借尺爵酌釈若寂弱主取守手朱殊狩珠種趣酒首儒受寿授樹需囚収周宗就州'
        '修愁拾秀秋終習臭舟衆襲週酬集醜住充十従柔汁渋獣縦重銃叔宿淑祝縮粛塾熟出'
        '術述俊春瞬准循旬殉準潤盾純巡遵順処初所暑庶緒署書諸助叙女序徐除傷償勝匠'
        '升召商唱奨宵将小少尚床彰承抄招掌昇昭晶松沼消渉焼焦照症省硝礁祥称章笑粧'
        '紹肖衝訟証詔詳象賞鐘障上丈乗冗剰城場壌嬢常情条浄状畳蒸譲醸錠嘱飾植殖織'
        '職色触食辱伸信侵唇娠寝審心慎振新森浸深申真神紳臣薪親診身辛進針震人仁刃'
        '尋甚尽迅陣酢図吹垂帥推水炊睡粋衰遂酔随髄崇数枢据杉澄寸世瀬畝是制勢姓征'
        '性成政整星晴正清牲生盛精聖声製西誠誓請逝青静斉税隻席惜斥昔析石積籍績責'
        '赤跡切拙接摂折設窃節説雪絶舌仙先千占宣専川戦扇栓泉浅洗染潜旋線繊船薦践'
        '選遷銭鮮前善漸然全禅繕塑措疎礎祖租粗素組訴阻僧創双倉喪壮奏層想捜掃挿操'
        '早曹巣槽燥争相窓総草荘葬藻装走送遭霜騒像増憎臓蔵贈造促側則即息束測足速'
        '俗属賊族続卒存孫尊損村他多太堕妥惰打駄体対耐帯待怠態替泰滞胎袋貸退逮隊'
        '代台大第題滝卓宅択拓沢濯託濁諾但達奪脱棚谷丹単嘆担探淡炭短端胆誕鍛団壇'
        '弾断暖段男談値知地恥池痴稚置致遅築畜竹蓄逐秩窒茶嫡着中仲宙忠抽昼柱注虫'
        '衷鋳駐著貯丁兆帳庁弔張彫徴懲挑朝潮町眺聴腸調超跳長頂鳥勅直朕沈珍賃鎮陳'
        '津墜追痛通塚漬坪釣亭低停偵貞呈堤定帝底庭廷弟抵提程締艇訂逓邸泥摘敵滴的'
        '笛適哲徹撤迭鉄典天展店添転点伝殿田電吐塗徒斗渡登途都努度土奴怒倒党冬凍'
        '刀唐塔島悼投搭東桃棟盗湯灯当痘等答筒糖統到討謄豆踏逃透陶頭騰闘働動同堂'
        '導洞童胴道銅峠匿得徳特督篤毒独読凸突届屯豚曇鈍内縄南軟難二尼弐肉日乳入'
        '如尿任妊忍認寧猫熱年念燃粘悩濃納能脳農把覇波派破婆馬俳廃拝排敗杯背肺輩'
        '配倍培媒梅買売賠陪伯博拍泊白舶薄迫漠爆縛麦箱肌畑八鉢発髪伐罰抜閥伴判半'
        '反帆搬板版犯班畔繁般藩販範煩頒飯晩番盤蛮卑否妃彼悲扉批披比泌疲皮碑秘罷'
        '肥被費避非飛備尾微美鼻匹必筆姫百俵標氷漂票表評描病秒苗品浜貧賓頻敏瓶不'
        '付夫婦富布府怖扶敷普浮父符腐膚譜負賦赴附侮武舞部封風伏副復幅服福腹複覆'
        '払沸仏物分噴墳憤奮粉紛雰文聞丙併兵塀幣平弊柄並閉陛米壁癖別偏変片編辺返'
        '遍便勉弁保舗捕歩補穂募墓慕暮母簿倣俸包報奉宝峰崩抱放方法泡砲縫胞芳褒訪'
        '豊邦飽乏亡傍剖坊妨帽忘忙房暴望某棒冒紡肪膨謀貿防北僕墨撲朴牧没堀奔本翻'
        '凡盆摩磨魔麻埋妹枚毎幕膜又抹末繭万慢満漫味未魅岬密脈妙民眠務夢無矛霧婿'
        '娘名命明盟迷銘鳴滅免綿面模茂妄毛猛盲網耗木黙目戻問紋門夜野矢厄役約薬訳'
        '躍柳愉油癒諭輸唯優勇友幽悠憂有猶由裕誘遊郵雄融夕予余与誉預幼容庸揚揺擁'
        '曜様洋溶用窯羊葉要謡踊陽養抑欲浴翌翼羅裸来頼雷絡落酪乱卵欄濫覧利吏履理'
        '痢裏里離陸律率立略流留硫粒隆竜慮旅虜了僚両寮料涼猟療糧良量陵領力緑倫厘'
        '林臨輪隣塁涙累類令例冷励礼鈴隷零霊麗齢暦歴列劣烈裂廉恋練連錬炉路露労廊'
        '朗楼浪漏老郎六録論和話賄惑枠湾腕挨曖宛嵐畏萎椅彙茨咽淫唄鬱怨媛艶旺岡臆'
        '俺苛牙瓦楷潰諧崖蓋骸柿顎葛釜鎌韓玩伎亀毀畿臼嗅巾僅錦惧串窟熊詣憬稽隙桁'
        '拳鍵舷股虎錮勾梗喉乞傲駒頃痕沙挫采塞埼柵刹拶斬恣摯餌鹿𠮟嫉腫呪袖羞蹴憧'
        '拭尻芯腎須裾凄醒脊戚煎羨腺詮箋膳狙遡曽爽痩踪捉遜汰唾堆戴誰旦綻緻酎貼嘲'
        '捗椎爪鶴諦溺塡妬賭藤瞳栃頓貪丼那奈梨謎鍋匂虹捻罵剝箸氾汎阪斑眉膝肘訃阜'
        '蔽餅璧蔑哺蜂貌頰睦勃昧枕蜜冥麺冶弥闇喩湧妖瘍沃拉辣藍璃慄侶瞭瑠呂賂弄籠'
        '麓脇').decode('utf8')

joyo_only = False

bmp_only = False

with open('cjk-decomp-0.4.0.txt', encoding='utf-8') as f:
    for line in f:
        m = format.match(line)
        char, dtype, dchars = [m.group(field)
                               for field in ['char', 'dtype', 'dchars']]
        dchars = dchars.split(',')
        if dtype not in ['a', 'd']:
            # Ignore entries with decomposition type other than 'across'
            # and 'down'
            continue
        if len(char) == 5:
            # Ignore non-Unicode intermediate decompositions
            continue
        if len(dchars) != 2:
            # Ignore entries with more than two components
            continue
        if any(len(c) == 5 for c in dchars):
            # Ignore entries with intermediate components
            continue
        if bmp_only and any(ord(c) > 0xffff for c in dchars + [char]):
            continue
        if joyo_only and any(c not in joyo for c in dchars + [char]):
            continue
        horizontal = dtype == 'a'
        center_chars[dchars[0]]['right' if horizontal else 'bottom'].add(char)
        center_chars[dchars[-1]]['left' if horizontal else 'top'].add(char)
        decomp[char] = dchars


def is_complete(ring):
    return all(d in ring for d in directions)

def random_center():
    while True:
        c = random.choice(center_chars.keys())
        ring = center_chars[c]
        if is_complete(ring):
            return c

def random_ring(c):
    ring = center_chars[c]
    if not is_complete(ring):
        return None
    return [random.choice(list(ring[d])) for d in directions]

def make_ring_text(center, trbl):
    t, r, b, l = [decomp[c][off] for c, off in zip(trbl, [0, 1, 1, 0])]
    return u'\u3000%s\n%s%s%s\n\u3000%s' % (t, l, center, r, b)

def make_snippet(c, trbl):
    return u'%s\n\n%s' % (' + '.join(trbl), make_ring_text(c, trbl))

def random_snippet():
    c = random_center()
    return make_snippet(c, random_ring(c))


if __name__ == '__main__':
    print 'Rings available for:'
    print ''.join(c for c, w in center_chars.iteritems() if is_complete(w))
    centers = [arg.decode('utf-8') for arg in sys.argv[1:]]
    if not centers:
        centers = random_center()
    for c in centers:
        trbl = random_ring(c)
        if trbl is None:
            print 'No ring possible for', c
            continue
        print make_snippet(c, trbl)
