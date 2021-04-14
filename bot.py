import telebot
import random
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot('1571975606:AAElyjPwbhtqvi8hU-uoRxZnVBsBwjKKC8A')

url = [['https://tramvaiiskusstv.ru/media/k2/galleries/198/2.jpg',
        'https://tramvaiiskusstv.ru/media/k2/galleries/198/3.jpg',
        'https://tramvaiiskusstv.ru/media/k2/galleries/198/4.jpg',
        'https://sun9-56.userapi.com/impf/Cz3G8F3L3bX9pD13Bb7YDJq2Bn7gJFCCuq_iWA/mZ_UBRk4Gwk.jpg?size=1132x822&quality=96&proxy=1&sign=450b1c175e88c82bc8e62c1c5d5bab01&type=album',
        'https://bidspirit-images.global.ssl.fastly.net/vnikitskom/cloned-images/84911/1/a_ignore_q_80_w_1000_c_limit_1.jpg',
        'https://rusmuseumvrm.ru/data/collections/museums/muzey_izobrazitelnih_iskusstv_komsomolsk-na-amure/kupriyanov_m.v._koktebel._plyazh._1958._komsomolsk-na-amure/14745_mainfoto_03.jpg',
        'https://sun9-36.userapi.com/impf/RY8sNdfsFFob-iyFtbIWQa8qnGfU2WyyjfmHMA/gRpibt5U4J0.jpg?size=1230x900&quality=96&proxy=1&sign=c88c08fd3672a175923aa4c4a1be749b&type=album',

        'https://sovcom.ru/pics/auctions/20613_45.jpg',
        'https://sovcom.ru/pics/auctions/4_59ba74c748660.jpg',
        'https://sovcom.ru/pics/auctions/75055_57.jpg',
        'https://sovcom.ru/pics/auctions/27148_140.jpg',
        'https://sovcom.ru/pics/auctions/25334_47.jpg'],
       ['https://upload.wikimedia.org/wikipedia/ru/0/0c/Беспощадно_разгромим_и_уничтожим_врага.jpg',
        'https://paintingplanet.ru/pictures/image1087_0.jpg',
        'https://rusmuseumvrm.ru/data/collections/painting/19_20/kukriniksi_begstvo_fashistov_iz_novgoroda_1944_1946_zh_5565/5971_mainfoto_03.jpg',
        'http://f.rodon.org/p/16/080815123619.jpg',
        'https://rusmuseumvrm.ru/data/collections/painting/19_20/kukriniksi._obvinenie._nyurenbergskiy_process._1967._zh-8928/24425_mainfoto_01.jpg'],
       [
           'http://www.art-auction.ru/files/services_pictures/244.jpg',
           'http://data14.gallery.ru/albums/gallery/37059-55017-60384760-m750x740-ue4871.jpg',
           'http://www.ratingtour.ru/i/photogallery/50/2391.jpg',
           'https://live.staticflickr.com/823/41646136372_b094e1b191_b.jpg',
           'http://4.bp.blogspot.com/-idht4UX_XhA/UokjltLRBYI/AAAAAAAAr6A/6zzT6ARM1d4/s1600/П.Н.+Крылов+Утро+на+Оке.jpg',
           'https://tmii-tula.ru/foto/z-krylov-raboti12big.jpg',
           'https://rusmuseumvrm.ru/data/collections/museums/istoriko-kraevedcheskiy_i_hudozhestvenniy_muzey_tula/krilov_p.n._karadag__vecher._1950._tula/14838_mainfoto_03.jpg',
           'https://rusmuseumvrm.ru/data/collections/museums/istoriko-kraevedcheskiy_i_hudozhestvenniy_muzey_tula/krilov_p.n._koktebel._karadag._1956._tula/14839_mainfoto_03.jpg',
           'https://cs12.pikabu.ru/post_img/2020/12/02/2/1606868378196245072.jpg',
           'https://lh3.googleusercontent.com/proxy/qaqGb15a_qws8C-E_PFti89WyRt7heBOQb3D-uPCfvCTiAeQn0KgtkgCt-w3tJRLv-KDB_sWxRlQ5IY',
           'http://4.bp.blogspot.com/-RLDumfPfQV4/Uf4O_TXp90I/AAAAAAAArMM/Px3LrX2yBO8/s640/тульский+музей4.jpg',
           'https://sovcom.ru/pics/auctions/32576_97.jpg',
           'https://i.pinimg.com/originals/9e/ee/8e/9eee8e09d9d3e5cab5853f785ee19157.png'],
       [
           'https://sun9-59.userapi.com/impf/3cTpxdWo2QoSKeE1LgNUkz5Gx6xdw6d9qXxoLw/K4XEVGB5LA0.jpg?size=1136x800&quality=96&proxy=1&sign=897a05dfea8a151b51c8d97026dd7ab0&type=album',
           'https://static.tildacdn.com/tild6336-3066-4331-b638-363830653366/864_________1940___5.jpg',
           'https://i.pinimg.com/564x/3a/2f/b2/3a2fb2d68f730122e7f28c9dacce4053.jpg'
       ],
       ['http://www.artcyclopedia.ru/img/big/008810131.jpg',
        'http://www.artcyclopedia.ru/img/big/008810140.jpg',
        'http://www.artcyclopedia.ru/img/big/008810146.jpg',
        'http://www.artcyclopedia.ru/img/big/008810147.jpg',
        'http://www.artcyclopedia.ru/img/big/008810150.jpg',
        'http://www.artcyclopedia.ru/img/big/008810157.jpg',
        'http://www.artcyclopedia.ru/img/big/008810158.jpg',
        'http://www.artcyclopedia.ru/img/big/008810161.jpg',
        'http://www.artcyclopedia.ru/img/big/008810181.jpg',
        'http://www.artcyclopedia.ru/img/big/008810182.jpg',
        'http://www.artcyclopedia.ru/img/big/008810183.jpg',
        'http://www.artcyclopedia.ru/img/big/008810184.jpg',
        'http://www.artcyclopedia.ru/img/big/008810185.jpg',
        'http://www.artcyclopedia.ru/img/big/008810186.jpg',
        'http://www.artcyclopedia.ru/img/big/008810188.jpg',
        'http://www.artcyclopedia.ru/img/big/008810189.jpg',
        'http://www.artcyclopedia.ru/img/big/008810191.jpg',
        'http://www.artcyclopedia.ru/img/big/008810192.jpg',
        'http://www.artcyclopedia.ru/img/big/008810193.jpg',
        'http://www.artcyclopedia.ru/img/big/008810194.jpg',
        'http://www.artcyclopedia.ru/img/big/008810195.jpg',
        'http://www.artcyclopedia.ru/img/big/008810196.jpg',
        'http://www.artcyclopedia.ru/img/big/008810197.jpg',
        'http://www.artcyclopedia.ru/img/big/008810198.jpg',
        'http://www.artcyclopedia.ru/img/big/008810201.jpg',
        'http://www.artcyclopedia.ru/img/big/008810202.jpg',
        'http://www.artcyclopedia.ru/img/big/008810205.jpg',
        'http://www.artcyclopedia.ru/img/big/008810210.jpg',
        'http://www.artcyclopedia.ru/img/big/008810223.jpg',
        'http://www.artcyclopedia.ru/img/big/008810234.jpg',
        'http://www.artcyclopedia.ru/img/big/008810236.jpg',
        'http://www.artcyclopedia.ru/img/big/008810257.jpg',
        'http://www.artcyclopedia.ru/img/big/008810263.jpg',
        'http://www.artcyclopedia.ru/img/big/008810267.jpg'

        ],
       [
           'https://upload.wikimedia.org/wikipedia/ru/7/7d/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D0%B0%D1%80%D0%BC%D0%B8%D1%8F_%28%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%B0_%D0%93%D0%B5%D1%80%D0%B0%D1%81%D0%B8%D0%BC%D0%BE%D0%B2%D0%B0%29.jpg',
           'https://upload.wikimedia.org/wikipedia/ru/thumb/0/09/A._Gerasimov_Stalin-and-Voroshilov.jpg/1280px-A._Gerasimov_Stalin-and-Voroshilov.jpg',
           'https://upload.wikimedia.org/wikipedia/ru/6/6f/%D0%93%D0%B5%D1%80%D0%B0%D1%81%D0%B8%D0%BC%D0%BE%D0%B2_%D0%90._%D0%9C.%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%BE%D0%B2%D0%BE%D0%B9_%D0%BF%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.jpg',
           'http://visualrian.ru/images/old_preview/75/38/753852_preview.jpg',
           'https://topkartin.ru/wp-content/uploads/2019/12/posledojdya.jpg',
           'http://www.museum.ru/imgB.asp?6165',
           'https://muzei-mira.com/templates/museum/images/paint/portret-baleriny-lepeshinskoy-gerasimov+.jpg',
           'https://lh3.googleusercontent.com/proxy/rYOR6cmiDURU38Le8CLPAWT_kOaswqqL0rOspzkMjRQOa4wz7fLyN7TdtC-6Zc0AezzUoc3r-O6Gscu_DMsSYV1jQ8MwSj1xEYuGYzYcaByKoEETWQ5reklaW9GeKwk_ZTrFilUDPvJEimPU',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a.m._gimn_oktyabryu._1942_zh-5846/11094_mainfoto_03.jpg',
           'https://regnum.ru/uploads/pictures/news/2016/11/28/regnum_picture_1480282404704988_normal.jpg',
           'https://shishkin-gallery.ru/upload/items/item_5769_4eb97863.jpg',
           'https://i.pinimg.com/originals/8a/29/1e/8a291e17a31a671be3fa036852b948ea.jpg',
           'https://историк.рф/uploads/picture/2020/11/22/thumbnails/pvLP2jPd44ir.jpg',
           'https://i.pinimg.com/originals/56/b7/97/56b7970780d120bbbb3ecabf0ef4ddd4.jpg',
           'https://mediashm.ru/wp-content/uploads/2016/02/8088.jpg?v=1614840400',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a_m_portret_a_k_tarasovoy_1939_zh_5939/2758_mainfoto_03.jpg',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a._m._bolshak._mezhdu_1900-mi_i_1956._zh-6704/17859_mainfoto_01.jpg',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a._m._polden._tepliy_dozhd._1939._zh-8049/17874_mainfoto_03.jpg',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a._m._portret_n._s._hanaeva._1945._zh-5578/17871_mainfoto_03.jpg',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a._m._zelenaya_rozh._1946._zh-5585/17864_mainfoto_03.jpg',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a._m._portret_k._e._voroshilova._1948._zh-6047/17870_mainfoto_03.jpg',
           'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_a._m._portret_b._i._yakovleva._1950._zh-5869/17869_mainfoto_03.jpg',
           'https://historyrussia.org/images/img-vystavki/vystavkagerasimov/13477.jpg',
           'https://historyrussia.org/images/img-vystavki/vystavkagerasimov/is3.jpg',
           'https://mstrok.ru/assets/mstrok_files_2/images/2017/05/05/24.jpg'
       ],
       ['https://www.tretyakovgallery.ru/upload/iblock/9c0/9c08afbc0351c527cd4d6ddb4a3603cc.jpg',
        'https://www.tretyakovgallery.ru/upload/iblock/d3f/d3fd41bae0390dcddbcb56973f0fcc04.jpg',
        'https://rusmuseumvrm.ru/data/collections/painting/19_20/gerasimov_s.v._v._i._lenin_na_ii_sezde_sovetov_sredi_delegatov-krestyan._19351936._zh-6149/16404_mainfoto_03.jpg',
        'http://www.mozhaysk.ru/image/gerasimov/Picture/120Sir.JPG',
        'https://upload.wikimedia.org/wikipedia/ru/d/dc/%D0%9C%D0%B0%D1%82%D1%8C_%D0%9F%D0%B0%D1%80%D1%82%D0%B8%D0%B7%D0%B0%D0%BD%D0%B0_2.png',
        'https://i.pinimg.com/564x/73/9d/54/739d5450b10189fb784247b11fb54b30.jpg',
        'https://rusmuseumvrm.ru/data/collections/museums/orenburgskiy_muzey_izobrazitelnih_iskusstv/gerasimov_s.v._sin_vernulsya._1947._omizo/23403_mainfoto_03.jpg',
        'https://rusmuseumvrm.ru/data/collections/museums/kemerovskiy_oblastnoy_muzey_izobrazitelnih_iskusstv_/gerasimov_s.v._ileckaya_zaschita._1943._komii/23487_mainfoto_03.jpg',
        'https://rusmuseumvrm.ru/data/collections/museums/orenburgskiy_muzey_izobrazitelnih_iskusstv/gerasimov_s.v._okolo_kozolinska.__13.02.1943._omizo/23406_mainfoto_03.jpg',
        'https://rusmuseumvrm.ru/data/collections/museums/orenburgskiy_muzey_izobrazitelnih_iskusstv/gerasimov_s.v._za_chkalovim._razezd.__12.11.1941._omizo/23405_mainfoto_03.jpg',
        'https://rusmuseumvrm.ru/data/collections/museums/orenburgskiy_muzey_izobrazitelnih_iskusstv/gerasimov_s.v._saksaulsk._1941._omizo/23407_mainfoto_03.jpg',
        'https://www.surikov-museum.ru/up/pictures/og_image/Prevyyu_33.jpg',
        'https://i.pinimg.com/originals/3e/9e/38/3e9e38b9b8ab78d2532f79684bfea73f.jpg',
        'http://www.artonline.ru/encyclopedia-data/prev/168-1.jpg',
        'http://www.artonline.ru/encyclopedia-data/prev/168-2.jpg',
        'http://www.artonline.ru/encyclopedia-data/prev/167-2.jpg',
        'https://ar.culture.ru/attachments/attachment/preview/5d96f6e421746c44fd65140e-preview.JPG'
        ],
       ['https://www.deineka.ru/images/works/jenski_portret.jpg',
        'https://upload.wikimedia.org/wikipedia/ru/e/e7/Раздолье_%28Дейнека%29.jpg',
        'https://www.deineka.ru/images/works/tekstilshitsy2.jpg',
        'https://web.archive.org/web/20160311132805im_/http://www.tretyakovgallery.ru/pictures/c/cc/ccf7f741870ab0b74558afe6baa964d9.jpg',
        'http://www.demoscope.ru/weekly/2006/0241/img/deineka.jpg',
        'https://www.deineka.ru/images/works/futbolist.jpg',
        'https://www.deineka.ru/images/works/652.jpg',
        'https://web.archive.org/web/20071201105323if_/http://painting.artyx.ru/art_painting/painting/item/f00/s00/e0000866/pic/000000.jpg',
        'http://www.deineka.ru/images/works/vratar.jpg',
        'https://www.deineka.ru/images/works/pioner_kursk.jpg',
        'https://www.deineka.ru/images/works/skuka.jpg',
        'https://artdaily.com/Fotos/galerias/293/Deinekab.jpg',
        'https://www.deineka.ru/images/works/nikitka.jpg',
        'https://upload.wikimedia.org/wikipedia/ru/0/04/После_боя_%28Дейнека%29.jpg',
        'https://www.deineka.ru/images/works/v_okkupatcii.jpg',
        'https://web.archive.org/web/20070810054617if_/http://photos.streamphoto.ru/f/6/5/w400_ebad80f245932610566d990a2df5856f.jpg',
        'https://www.deineka.ru/images/works/na_prostorah_podmosk_stroek.jpg',
        'https://www.deineka.ru/images/works/v_sevastopole.jpg',
        'https://upload.wikimedia.org/wikipedia/ru/d/d0/Дейнека_оборона_Севастополя.jpg',
        'https://upload.wikimedia.org/wikipedia/ru/9/9f/Эстафета_по_кольцу_Б.jpg',
        'https://www.deineka.ru/images/works/dvor.jpg',
        'https://www.deineka.ru/images/works/portret_vyalova.jpg',
        'https://www.deineka.ru/images/works/kursk_posle_dojdya.jpg',
        'https://www.deineka.ru/images/works/posle_dojdya.jpg',
        'https://www.deineka.ru/images/works/222.jpg',
        'https://www.deineka.ru/images/works/pejzaj.jpg',
        'https://www.deineka.ru/images/works/krymski_peizaj.jpg',
        'https://www.deineka.ru/images/works/644.jpg',
        'https://www.deineka.ru/images/works/712.jpg',
        'https://www.deineka.ru/images/works/nayomnik_interventov.jpg',
        'https://www.deineka.ru/images/works/248.jpg',
        'https://www.deineka.ru/images/works/bombovoz.jpg',
        'https://www.deineka.ru/images/works/igra_v_myach.jpg',
        'https://www.deineka.ru/images/works/mother.jpg',
        'https://www.deineka.ru/images/works/v_vozduhe.jpg',
        'https://www.deineka.ru/images/works/648.jpg',
        'https://www.deineka.ru/images/works/713.jpg',
        'https://www.deineka.ru/images/works/otdyhaushie_deti.jpg',
        'https://www.deineka.ru/images/works/160.jpg',
        'https://www.deineka.ru/images/works/649.jpg',
        'https://www.deineka.ru/images/works/653.jpg',
        'https://www.deineka.ru/images/works/gidroplany_nad_korablyami.jpg',
        'https://www.deineka.ru/images/works/groza_zahodit.jpg',
        'https://www.deineka.ru/images/works/kolhoznoe_sobranie.jpg',

        'https://www.deineka.ru/images/works/krymsie_pionery.jpg',
        'https://www.deineka.ru/images/works/256.jpg',
        'https://www.deineka.ru/images/works/262.jpg',
        'https://www.deineka.ru/images/works/657.jpg',
        'https://www.deineka.ru/images/works/715.jpg',
        'https://www.deineka.ru/images/works/716.jpg',
        'https://www.deineka.ru/images/works/717.jpg',
        'https://www.deineka.ru/images/works/kolhoznitca_na_velosipede.jpg',
        'https://www.deineka.ru/images/works/721.jpg',
        'https://www.deineka.ru/images/works/geroi_pervoi_pyatiletki.jpg',
        'https://www.deineka.ru/images/works/na_jenskom_sobranii.jpg',
        'https://www.deineka.ru/images/works/portret_shervinskoy.jpg',
        'https://www.deineka.ru/images/works/stahanovtsy.jpg',
        'https://www.deineka.ru/images/works/krasnokrylyi_gigant.jpg',
        'https://www.deineka.ru/images/works/300.jpg',
        'https://www.deineka.ru/images/works/nad_snegami.jpg',
        'https://www.deineka.ru/images/works/774.jpg',
        'https://www.deineka.ru/images/works/766.jpg',
        'https://www.deineka.ru/images/works/768.jpg',
        'https://www.deineka.ru/images/works/levy_marsh.jpg',
        'https://www.deineka.ru/images/works/665.jpg',
        'https://www.deineka.ru/images/works/666.jpg',
        'https://www.deineka.ru/images/works/669.jpg',
        'https://www.deineka.ru/images/works/oda_vesne.jpg',
        'https://www.deineka.ru/images/works/681.jpg',
        'https://www.deineka.ru/images/works/devushki_v_vyhodnye_dni.jpg',
        'https://www.deineka.ru/images/works/730.jpg',
        'https://www.deineka.ru/images/works/moskva.jpg',
        'https://www.deineka.ru/images/works/352.jpg',
        'https://www.deineka.ru/images/works/traktorist.jpg',
        'https://www.deineka.ru/images/works/v_krymu.jpg',
        'https://www.deineka.ru/images/works/700.jpg',
        'https://www.deineka.ru/images/works/doyarka.jpg',
        'https://www.deineka.ru/images/works/734.jpg',
        'https://www.deineka.ru/images/works/701.jpg',
        'https://www.deineka.ru/images/works/pokoriteli_kosmosa.jpg',
        'https://www.deineka.ru/images/works/737.jpg',
        'https://www.deineka.ru/images/works/basketball.jpg',
        'https://www.deineka.ru/images/works/vse_flagi_v_gosti.jpg',
        'https://www.deineka.ru/images/works/uny_constructor.jpg',
        'https://www.deineka.ru/images/works/703.jpg'









        ],
       ['https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Второй_конгресс_Коминтерна.jpg/1920px-Второй_конгресс_Коминтерна.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Brodski_lenin.jpg/1920px-Brodski_lenin.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/6/69/Lenin_at_Putilov_factory_at_May_1917_%28better_res%29.jpg',
        'https://cdn.gallerix.asia/sr/B/1582512849/7697.jpg',
        'http://nv.ua/img/article/325/48_main.jpg',
        'https://i.pinimg.com/originals/48/65/16/486516a23207f281372535a1d9099288.jpg',
        'https://sr.gallerix.ru/B/1582512849/960556937.jpg',
        'http://visualrian.ru/images/old_preview/56/62/566208_preview.jpg',
        'https://rusmuseumvrm.ru/data/collections/painting/19_20/brodskiy_i.i._lenin_na_tribune._1927._zhs-729/16451_mainfoto_03.jpg',
        'https://opisanie-kartin.com/pictures/9/image020.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/1st_May_demonstration_by_Isaak_Brodsky_%281934%2C_GTG%29.jpg/412px-1st_May_demonstration_by_Isaak_Brodsky_%281934%2C_GTG%29.jpg,'
        'https://rusmuseumvrm.ru/data/collections/drawings/brodskiy_i._i.__v._i._lenin._na_krasnoy_ploschadi._1924._rs-19706/20039_mainfoto_03.jpg',
        'https://sr.gallerix.ru/B/1582512849/9834.jpg',
        'https://rossaprimavera.ru/static/files/07155fab5352.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Lenin_and_manifistation_by_Isaak_Brodsky_%281919%2C_GIM%29.jpg/800px-Lenin_and_manifistation_by_Isaak_Brodsky_%281919%2C_GIM%29.jpg',
        'https://muzei.club/wp-content/uploads/2020/04/fmg5ea94dab7ec0f9.jpeg'

        ],
       ['http://www.leningradschool.com/ant38b.jpg',
        'http://www.leningradschool.com/ant15b.jpg',
        'http://www.leningradschool.com/len104b.jpg',
        'http://www.leningradschool.com/ant34b.jpg'
        ]
       ]

description = [['«Прибытие поезда», 1931г.',
                '«На станции», 1930–1933 гг.',
                '«Паровоз», конец 1920-х – начало 1930-х гг.',
                '«Светает», 1957г.',
                '«Пейзаж с рекой», 1968г.',
                '«Коктебель. Пляж», 1958г.',
                '«Абрамцево», 1948г.',
                '«Абрамцево», 1948г.',
                '«Плес», 1947г.',
                '«Лунный вечер. Геническ», 1956г.',
                '«Геническ», 1977г.',
                '«Геническ», 1952г.'],
               [
                   '«Беспощадно разгромим и уничтожим врага!», 1941г.',
                   '«Таня», 1947г',
                   '«Бегство немцев из Новгорода», 1944–1946 гг.',
                   '«Конец», 1947–1948 гг.',
                   '«Обвинение. Нюрнбергский процесс», 1967г.'
               ],
               [
                   '«Тихо», 1941г.',
                   '«Зимнее поле», 1983г.',
                   '«Венеция», 1957г',
                   '«На веранде», 1973г.',
                   '«Утро на Оке», 1946г.',
                   '«Коктебельское утро», год неизвестен.',
                   '«Карадаг — вечер», 1950г.',
                   '«Коктебель. Карадаг», 1956г.',
                   '«Коктебель. Полдень», 1965г.',
                   '«Ненюфары», 1955г.',
                   '«Розы и синие сливы», 1962г.',
                   '«Алёнушка», 1985г.',
                   '«Оттепель», 1957г.'
               ],
               [
                   '«Лермонтовские места», 1964г.',
                   '«Примулы на окне», 1940г.',
                   '«Интерьер. Рыбинск», 1920г.'

               ],
               ['«Провинциалки», 1920г.',
                '«Утро в деревне. Хозяйка. Казань», 1920-е',
                '«Новая планета» или «Рождение новой планеты», 1921г.',
                '«Рождение новой планеты», 1921г.',
                '«Августовский вечер», 1922г.',
                '«Люди», 1923г.',
                '«Парад Красной армии», 1923г.',
                '«Сельский праздник. На горе. Лихачёво», 1923г.',
                '«Июль. Купание», 1925г.',
                '«Радуга. Лихачёво», 1925г.',
                '«В те дни. У Дома союзов в дни похорон В. И. Ленина», 1926г.',
                '«Комсомолки», 1926г.',
                '«Перед вступлением в Кремль. Никольские ворота», 1926г.',
                '«Подмосковная молодежь», 1926г.',
                '«Вступление в Кремль через Троицкие ворота 2 (15) ноября 1917 года», 1927г.',
                '«Первое появление В.И.Ленина на засед. Петросовета в Смольном 25 окт. 1917 г.», 1927г.',
                '«Окно в природу. Лихачёво», 1928г.',
                '«Первые колхозницы. В лучах солнца. Подолино», 1928г.',
                '«Праздник кооперации в деревне», 1928г.',
                '«Проводы рабочего отряда на фронт», 1928г.',
                '«Сбор яблок», 1928г.',
                '«Вступление в Кремль через Троицкие ворота 2(15) ноября 1917 года», 1929г.',
                '«Вузовцы», 1929г.',
                '«Конец зимы. Полдень. Лихачёво», 1929г.',
                '«Сени. Лигачёво», 1929г.',
                '«Уходящая провинция», 1929г.',
                '«Возвращение с работы», 1930г.',
                '«Первомайская демонстрация на Красной площади в 1929 году», 1930г.',
                '«Первое выступление В. И. Ленина в Смольном», 1935г.',
                '«Парад на Красной площади 7 ноября 1941 года», 1942г.',
                '«Утро Москвы», 1942г.',
                '«Штурм Кремля в 1917 году», 1947г.',
                '«Утро индустриальной Москвы», 1949г.',
                '«Штурм Кремля в 1917 году», 1951г.'

                ],
               ['«Первая конная армия», 1935г.',
                '«И. В. Сталин и К. Е. Ворошилов в Кремле» или «Иосиф Виссарионович Сталин и Климент Ефремович Ворошилов на прогулке в Кремле», 1938г.',
                '«Портрет старейших художников», 1944г.',
                '«Ленин на трибуне», 1929–1930гг.',
                '«После дождя» или «Мокрая терраса», 1935г.',
                '«Баня», 1938г.',
                '«Портрет балерины О. В. Лепешинской», 1939г.',
                '«И. В. Сталин и А. М. Горький в Горках», 1939г.',
                '«Гимн Октябрю», 1942г.',
                '«Тегеранская конференция руководителей трёх великих держав», 1945г.',
                '«Рожь», 1946г.',
                '«И. В. Сталин у гроба А. А. Жданова», 1948г.',
                '«Есть метро!», 1949г.',
                '«Вести с целины», 1954г.',
                '«Половецкие пляски», 1955г.',
                '«Портрет А. К. Тарасовой», 1939г.',
                '«Большак», между 1900-ми и 1956гг.',
                '«Полдень. Теплый дождь», 1939г.',
                '«Портрет Н. С. Ханаева», 1945г.',
                '«Зелёная рожь», 1946г.',
                '«Портрет К. Е. Ворошилова», 1948г.',
                '«Портрет Б. И. Яковлева», 1950г.',
                '«Розы», 1948г.',
                '«Портрет И. В. Сталина на XVII съезде ВКП(б)», 1934 г.',
                '«Портрет Героя Советского Союза Марии Щербаченко», 1944г.'],
               ['«Колхозный праздник», 1937г.',
                '«Лёд прошёл», 1945г.',
                '«В. И. Ленин на II съезде Советов среди делегатов-крестьян», 1935–1936гг.',
                '«Сирень в цвету», 1955г.',
                '«Мать партизана», 1943–1950гг.',
                '«Групповой портрет героев СССР В. Гризодубовой, П. Осипенко, М. Расковой», 1938г.',
                '«Сын вернулся», 1947г.',
                '«Илецкая защита», 1943г.',
                '«Около Козлинска», 1943г.',
                '«За Чкаловым. Разъезд», 1941–1943гг.',
                '«Саксаульск», 1941г.',
                '«Лето. Можайск», 1950г.',
                '«Фронтовик», 1926г.',
                '«Клятва сибирских партизан», 1933г.',
                '«Хлеб насущный», 1921г.',
                '«Северный пейзаж», 1933г.',
                '«Кисловодск. Центральная площадь», 1938г.'
                ],
               ['«Женский портрет», 1920г.',
                '«Раздолье», 1944г.',
                '«Текстильщицы», 1927г.',
                '«Оборона Петрограда», 1964г.',
                '«Спящий ребёнок с васильками», 1932г.',
                '«Футболист», 1932г.',
                '«Сельский пейзаж с коровами», 1933г.',
                '«Бегуны», 1934г.',
                '«Вратарь», 1934г.',
                '«Пионер», 1934г.',
                '«Скука», 1935г.',
                '«Будущие лётчики», 1938г.',
                '«Никитка», 1940г.',
                '«После боя» или «Купальщики» или «После душа» или «Душ. После боя», 1937–1942гг.',
                '«В оккупации», 1944г.',
                '«Донбасс», 1947г.',
                '«На просторах подмосковных строек», 1949г.',
                '«В Севастополе», 1956г.',
                '«Оборона Севастополя», 1942г.',
                '«Эстафета» или «Эстафета по кольцу „Б“» или Эстафета по Садовому кольцу», 1947г.',
                '«Двор», 1920г.',
                '«Портрет К. А. Вялова», 1923г.',
                '«Курск. После дождя», 1925г.',
                '«После дождя. Курск», 1925г.',
                '«Рабочий и крестьянин», 1927г.',
                '«Пейзаж», 1929г.',
                '«Крымский пейзаж», 1930г.',
                '«Поезд прошел. Из поезда», 1930г.',
                '«Дорога на юг», 1930г.',
                '«Наёмник интервентов», 1931г.',
                '«Бега», 1931г.',
                '«Бомбовоз», 1932г.',
                '«Игра в мяч», 1932г.',
                '«Мать», 1932г.',
                '«В воздухе», 1932г.',
                '«Утренняя зарядка», 1932г.',
                '«Подмосковье», 1932г.',
                '«Отдыхающие дети», 1933г.',
                '«Девочка у окна. Зима», 1933г.',
                '«Вечер. Ужгород», 1933г.',
                '«Солнечный день», 1933г.',
                '«Гидропланы над кораблями», 1934г.',
                '«Гроза заходит. Дождь», 1934г.',
                '«Колхозное собрание», 1934г.',
                '«Крымские пионеры», 1934г.',
                '«Совхоз. Новые дома», 1934г.',
                '«Севастополь. Порт», 1934г.',
                '«Портрет девушки с книгой», 1934г.',
                '«Физкультурники», 1934г.',
                '«Танец», 1934г.',
                '«Два класса», 1934г.',
                '«Колхозница на велосипеде», 1935г.',
                '«Портрет С. И. Лычёвой», 1935г.',
                '«Герои первой пятилетки», 1936г.',
                '«На женском собрании», 1937г.',
                '«Портрет Шервинской», 1937г.',
                '«Стахановцы», 1937г.',
                '«Краснокрылый гигант», 1938г.',
                '«Ленин на прогулке с детьми», 1938г.',
                '«Над льдиной папанинцев», 1938г.',
                '«В кабине», 1938г.',
                '«Летающая лодка», 1940г.',
                '«Пассажирский самолёт», 1940г.',
                '«Левый марш», 1941г.',
                '«Бегущие девушки», 1941г.',
                '«Тревожные ночи», 1942г.',
                '«Едут на войну», 1944г.',
                '«Ода весне», 1945г.',
                '«Колхозницы роют рвы», 1946–1947гг.',
                '«Девушки в выходные дни», 1949г.',
                '«Из школы», 1950г.',
                '«Москва», 1952г.',
                '«Портрет архитектора Тамары Милешиной», 1955г.',
                '«Тракторист», 1956г.',
                '«В Крыму», 1956г.',
                '«Кузнецы», 1957г.',
                '«Доярка», 1959г.',
                '«21 января 1924 года», 1959г.',
                '«Встреча с прекрасным», 1960г.',
                '«Покорители космоса», 1961г.',
                '«На учёбе», 1961г.',
                '«Баскетбол», 1962г.',
                '«Все флаги в гости будут к нам», 1964г.',
                '«Юный конструктор», 1966г.',
                '«Портрет молодого инженера», 1966г.'













                ],
               ['«Торжественное открытие II конгресса Коминтерна во дворце Урицкого в Ленинграде» или «II конгресс Коминтерна», 1920–1924гг',
                '«В. И. Ленин в Смольном», 1930г.',
                '«Выступление В. И. Ленина на митинге рабочих Путиловского завода в мае 1917 года», 1929г.',
                '«Летний сад осенью», 1928г.',
                '«Суд крестьян-батраков», 1931г.',
                '«Ассамблея Революционного Военного Совета СССР под председательством К. Е. Ворошилова», 1928г.',
                '«Ударник труда Днепростроя», 1932г.',
                '«В. И. Ленин на трибуне 1 мая 1920 года», 1933г.',
                '«Ленин на трибуне», 1927г.',
                '«Ленин на трибуне», 1930г.',
                '«Первомайская демонстрация», 1934г.',
                '«В. И. Ленин. На Красной площади», 1924г.',
                '«Портрет Сталина», 1933г.',
                '«Передача знамени парижских коммунаров московским рабочим на Ходынке», после 1924г.',
                '«Ленин и манифестация», 1919г.',
                '«Портрет М. Горького», 1937г.'

                ],
               ['«Девушка в саду», 1964г.',
                '«Девушка из Переяславля», 1964г.',
                '«Официантка», 1964г.',
                '«Солнечный день», 1982г.']
               ]

creators = ['Михаил Васильевич Куприянов', 'Кукрыниксы', 'Крылов Порфирий Никитич', 'Соколов Николай Александрович',
            'Константин Фёдорович Юон', 'Александр Михайлович Герасимов', 'Сергей Васильевич Герасимов', 'Александр Александрович Дейнека',
            'Исаак Израилевич Бродский','Евгения Петровна Антипова']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пробный вариант (!)\n'
                                      'Привет, дорогой ценитель соцреализма! Здраствуй, милая поклонница соцреализма!'
                                      'Я появился на свет в начале 2021 года, и мои технические родители хотели моим рождением дать новый толчок к изучению социалистического реализма. Так оставь предрассудки всяк сюда входящий! Изучай сам, но и поделиться с друзьями обо мне не забывай!)'
                                      'Чтобы увидеть, чем богат мой функционал натыкай по клавиатуре следующую команду: /help')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Команда \n'
                                      '/rand выводит пять случайных картин пяти случайных художников \n'
                                      '/name <фамилия художника> выводит случайную картину данного художника \n'
                                      '/list даёт список имеющихся в моей компьютерной памяти художников соцреализма \n')


@bot.message_handler(commands=['list'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Список художников: \n" 'Михаил Васильевич Куприянов \n' 'Кукрыниксы\n' 'Крылов Порфирий Никитич\n''Соколов Николай Александрович\n'
                     'Константин Фёдорович Юон \n' 'Александр Михайлович Герасимов\n' 'Сергей Васильевич Герасимов\n ' 
                     'Александр Александрович Дейнека \n'
                     'Исаак Израилевич Бродский \n' 'Евгения Петровна Антипова \n')


@bot.message_handler(commands=['rand'])
def start_message(message):
    randname = random.randint(0, len(creators) - 1)
    randother = random.randint(0, len(url[randname]) - 1)
    pic1 = url[randname][randother]
    str1 = str(creators[randname]) + '. ' + str(description[randname][randother])
    randname = random.randint(0, len(creators) - 1)
    randother = random.randint(0, len(url[randname]) - 1)
    pic2 = url[randname][randother]
    str2 = str(creators[randname]) + '. ' + str(description[randname][randother])
    randname = random.randint(0, len(creators) - 1)
    randother = random.randint(0, len(url[randname]) - 1)
    pic3 = url[randname][randother]
    str3 = str(creators[randname]) + '. ' + str(description[randname][randother])
    randname = random.randint(0, len(creators) - 1)
    randother = random.randint(0, len(url[randname]) - 1)
    pic4 = url[randname][randother]
    str4 = str(creators[randname]) + '. ' + str(description[randname][randother])
    randname = random.randint(0, len(creators) - 1)
    randother = random.randint(0, len(url[randname]) - 1)
    pic5 = url[randname][randother]
    str5 = str(creators[randname]) + '. ' + str(description[randname][randother])
    media = [InputMediaPhoto(pic1,
                             caption='1. ' + str1 + '\n' + '2. ' + str2 + '\n' + '3. ' + str3 + '\n' + '4. ' + str4 +
                                     '\n' + '5. ' + str5),
             InputMediaPhoto(pic2), InputMediaPhoto(pic3), InputMediaPhoto(pic4), InputMediaPhoto(pic5)]
    bot.send_media_group(message.chat.id, media)


@bot.message_handler(commands=['name'])
def start_message(message):
    if "куприянов" in message.text.lower():
        randinteger = random.randint(0, len(url[0]) - 1)
        print(randinteger)
        print(url[0][randinteger])

        bot.send_photo(message.chat.id, url[0][randinteger], creators[0] + '. ' + description[0][randinteger])
    elif 'кукрыниксы' in message.text.lower():
        print(len(url[1]), len(description[1]))
        randinteger = random.randint(0, len(url[1]) - 1)
        bot.send_photo(message.chat.id, url[1][randinteger], creators[1] + '. ' + description[1][randinteger])

    elif 'крылов' in message.text.lower():
        print(len(url[2]), len(description[2]))
        randinteger = random.randint(0, len(url[2]) - 1)
        bot.send_photo(message.chat.id, url[2][randinteger], creators[2] + '. ' + description[2][randinteger])

    elif 'соколов' in message.text.lower():
        print(len(url[3]), len(description[3]))
        randinteger = random.randint(0, len(url[3]) - 1)
        bot.send_photo(message.chat.id, url[3][randinteger], creators[3] + '. ' + description[3][randinteger])

    elif 'юон' in message.text.lower():
        print(len(url[4]), len(description[4]))
        randinteger = random.randint(0, len(url[4]) - 1)
        bot.send_photo(message.chat.id, url[4][randinteger], creators[4] + '. ' + description[4][randinteger])
    elif 'герасимов' in message.text.lower() and 'александр' in message.text.lower():
        print(len(url[5]), len(description[5]))
        randinteger = random.randint(0, len(url[5]) - 1)
        bot.send_photo(message.chat.id, url[5][randinteger], creators[5] + '. ' + description[5][randinteger])
    elif 'герасимов' in message.text.lower() and 'сергей' in message.text.lower():
        print(len(url[6]), len(description[6]))
        randinteger = random.randint(0, len(url[6]) - 1)
        bot.send_photo(message.chat.id, url[6][randinteger], creators[6] + '. ' + description[6][randinteger])
    elif 'герасимов' in message.text.lower():
        bot.send_message(message.chat.id,
                         "Я знаю даже двух прекрасных художников с фамилией Герасимов! Уточните, пожалуйста, картины какого из них вы хотите увидеть! Есть Александр Михайлович Герасимов и Сергей Васильевич Герасимов")
    elif 'дейнека' in message.text.lower() :
        print(len(url[7]), len(description[7]))
        randinteger = random.randint(0, len(url[7]) - 1)
        bot.send_photo(message.chat.id, url[7][randinteger], creators[7] + '. ' + description[7][randinteger])
    elif 'бродский' in message.text.lower() :
        print(len(url[7]), len(description[8]))
        randinteger = random.randint(0, len(url[8]) - 1)
        bot.send_photo(message.chat.id, url[8][randinteger], creators[8] + '. ' + description[8][randinteger])

@bot.message_handler(content_types=['text'])
def send_text(message):
    flag = False

    for i in range(len(creators)):
        for j in range(len(description[i])):
            if message.text.lower() in description[i][j].lower():
                flag = True
                bot.send_photo(message.chat.id, url[i][j], creators[i] + '. ' + description[i][j])
    if not flag:
        bot.send_message(message.chat.id, 'Картины с таким названием нет в нашей базе данных')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
