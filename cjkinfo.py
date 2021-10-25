# -*- coding: utf-8 -*-

'''Utility constants'''

import re

# Characters in CJK Unified Ideographs that are radicals and not full
# characters (compiled manually; probably not exhaustive)
radicals = (
    u'㔾䒑丨丬丶丷乚乛亠亻冖冫凵刂勹卄卩厶夂宀幺廴廾彐彡忄扌氵氺灬爫爿犭礻糹纟罒罓耂艹衤覀讠豸辶钅阝飠饣')

# Regex matching characters for which glyphs are included on iOS 15.0 and
# Android SDK 31. See: https://github.com/amake/CodePointCoverage
mobile_ok = re.compile(r'[\u0000-\u0019\u0020-\u007e\u00a0-\u0377\u037a-\u037f\u0384-\u038a\u038c\u038e-\u03a1\u03a3-\u052f\u0531-\u0556\u0559-\u055f\u0561-\u0587\u0589-\u058a\u058d-\u058f\u0591-\u05c7\u05d0-\u05ea\u05f0-\u05f4\u0600-\u0604\u0606-\u061c\u061e-\u070d\u070f-\u074a\u074d-\u07b1\u07c0-\u07fa\u0800-\u082d\u0830-\u083e\u0840-\u085b\u085e\u08a0\u08a2-\u08ac\u08e4-\u08f9\u08fb-\u08fe\u0900-\u0983\u0985-\u098c\u098f-\u0990\u0993-\u09a8\u09aa-\u09b0\u09b2\u09b6-\u09b9\u09bc-\u09c4\u09c7-\u09c8\u09cb-\u09ce\u09d7\u09dc-\u09dd\u09df-\u09e3\u09e6-\u09fb\u0a01-\u0a03\u0a05-\u0a0a\u0a0f-\u0a10\u0a13-\u0a28\u0a2a-\u0a30\u0a32-\u0a33\u0a35-\u0a36\u0a38-\u0a39\u0a3c\u0a3e-\u0a42\u0a47-\u0a48\u0a4b-\u0a4d\u0a51\u0a59-\u0a5c\u0a5e\u0a66-\u0a75\u0a81-\u0a83\u0a85-\u0a8d\u0a8f-\u0a91\u0a93-\u0aa8\u0aaa-\u0ab0\u0ab2-\u0ab3\u0ab5-\u0ab9\u0abc-\u0ac5\u0ac7-\u0ac9\u0acb-\u0acd\u0ad0\u0ae0-\u0ae3\u0ae6-\u0af1\u0af9\u0b01-\u0b03\u0b05-\u0b0c\u0b0f-\u0b10\u0b13-\u0b28\u0b2a-\u0b30\u0b32-\u0b33\u0b35-\u0b39\u0b3c-\u0b44\u0b47-\u0b48\u0b4b-\u0b4d\u0b56-\u0b57\u0b5c-\u0b5d\u0b5f-\u0b63\u0b66-\u0b77\u0b82-\u0b83\u0b85-\u0b8a\u0b8e-\u0b90\u0b92-\u0b95\u0b99-\u0b9a\u0b9c\u0b9e-\u0b9f\u0ba3-\u0ba4\u0ba8-\u0baa\u0bae-\u0bb9\u0bbe-\u0bc2\u0bc6-\u0bc8\u0bca-\u0bcd\u0bd0\u0bd7\u0be6-\u0bfa\u0c00-\u0c03\u0c05-\u0c0c\u0c0e-\u0c10\u0c12-\u0c28\u0c2a-\u0c39\u0c3d-\u0c44\u0c46-\u0c48\u0c4a-\u0c4d\u0c55-\u0c56\u0c58-\u0c5a\u0c60-\u0c63\u0c66-\u0c6f\u0c78-\u0c83\u0c85-\u0c8c\u0c8e-\u0c90\u0c92-\u0ca8\u0caa-\u0cb3\u0cb5-\u0cb9\u0cbc-\u0cc4\u0cc6-\u0cc8\u0cca-\u0ccd\u0cd5-\u0cd6\u0cde\u0ce0-\u0ce3\u0ce6-\u0cef\u0cf1-\u0cf2\u0d02-\u0d03\u0d05-\u0d0c\u0d0e-\u0d10\u0d12-\u0d3a\u0d3d-\u0d44\u0d46-\u0d48\u0d4a-\u0d4e\u0d57\u0d60-\u0d63\u0d66-\u0d75\u0d79-\u0d7f\u0d82-\u0d83\u0d85-\u0d96\u0d9a-\u0db1\u0db3-\u0dbb\u0dbd\u0dc0-\u0dc6\u0dca\u0dcf-\u0dd4\u0dd6\u0dd8-\u0ddf\u0df2-\u0df4\u0e01-\u0e3a\u0e3f-\u0e5b\u0e81-\u0e82\u0e84\u0e87-\u0e88\u0e8a\u0e8d\u0e94-\u0e97\u0e99-\u0e9f\u0ea1-\u0ea3\u0ea5\u0ea7\u0eaa-\u0eab\u0ead-\u0eb9\u0ebb-\u0ebd\u0ec0-\u0ec4\u0ec6\u0ec8-\u0ecd\u0ed0-\u0ed9\u0edc-\u0edd\u0f00-\u0f47\u0f49-\u0f6c\u0f71-\u0f8b\u0f90-\u0f97\u0f99-\u0fbc\u0fbe-\u0fcc\u0fce-\u0fd8\u1000-\u10c5\u10d0-\u1112\u115f-\u1175\u119e\u11a2\u11a8-\u11c2\u1200-\u1248\u124a-\u124d\u1250-\u1256\u1258\u125a-\u125d\u1260-\u1288\u128a-\u128d\u1290-\u12b0\u12b2-\u12b5\u12b8-\u12be\u12c0\u12c2-\u12c5\u12c8-\u12d6\u12d8-\u1310\u1312-\u1315\u1318-\u135a\u135d-\u137c\u1380-\u1399\u13a0-\u13f5\u13f8-\u13fd\u1401-\u1676\u1680-\u169c\u16a0-\u16f0\u1700-\u170c\u170e-\u1714\u1720-\u1736\u1740-\u1753\u1760-\u176c\u176e-\u1770\u1772-\u1773\u1780-\u17dd\u17e0-\u17e9\u17f0-\u17f9\u1800-\u180e\u1810-\u1819\u1820-\u1877\u1880-\u18aa\u1900-\u191c\u1920-\u192b\u1930-\u193b\u1940\u1944-\u196d\u1970-\u1974\u1980-\u19ab\u19b0-\u19c9\u19d0-\u19da\u19de-\u1a1b\u1a1e-\u1a5e\u1a60-\u1a7c\u1a7f-\u1a89\u1a90-\u1a99\u1aa0-\u1aad\u1b00-\u1b4b\u1b50-\u1b7c\u1b80-\u1bf3\u1bfc-\u1c37\u1c3b-\u1c49\u1c4d-\u1c7f\u1c90-\u1cba\u1cbd-\u1cc7\u1cd0\u1cd2-\u1cd3\u1cd7\u1cd9-\u1cda\u1cdc-\u1cdd\u1ce0\u1cf2-\u1cf5\u1cf8-\u1cf9\u1d00-\u1dca\u1dcd\u1dfe-\u1f15\u1f18-\u1f1d\u1f20-\u1f45\u1f48-\u1f4d\u1f50-\u1f57\u1f59\u1f5b\u1f5d\u1f5f-\u1f7d\u1f80-\u1fb4\u1fb6-\u1fc4\u1fc6-\u1fd3\u1fd6-\u1fdb\u1fdd-\u1fef\u1ff2-\u1ff4\u1ff6-\u1ffe\u2000-\u2027\u202a-\u205f\u206a-\u2071\u2074-\u208e\u2090-\u209c\u20a0-\u20bf\u20d0-\u20e1\u20e3-\u20f0\u2100-\u214e\u2150-\u2184\u2189\u2190-\u23e7\u23e9-\u23f3\u23f8-\u23fa\u2400-\u2426\u2440-\u244a\u2460-\u269c\u26a0-\u26b2\u26bd-\u26be\u26c4-\u26c5\u26c8\u26cb\u26ce-\u26cf\u26d1\u26d3-\u26d4\u26e2\u26e9-\u26ea\u26f0-\u26f5\u26f7-\u26fa\u26fd\u2701-\u275e\u2761-\u27cd\u27d0-\u2b4c\u2b50-\u2b55\u2b58\u2b95\u2c00-\u2c2e\u2c30-\u2c5e\u2c60-\u2c71\u2c74-\u2c77\u2c79-\u2c7a\u2c7c-\u2c7d\u2c80-\u2cf3\u2cf9-\u2cff\u2d30-\u2d67\u2d6f-\u2d70\u2d7f-\u2d96\u2da0-\u2da6\u2da8-\u2dae\u2db0-\u2db6\u2db8-\u2dbe\u2dc0-\u2dc6\u2dc8-\u2dce\u2dd0-\u2dd6\u2dd8-\u2dde\u2de0-\u2e18\u2e1c-\u2e1d\u2e28-\u2e29\u2e2e\u2e30-\u2e31\u2e3a-\u2e3b\u2e40-\u2e41\u2e80-\u2e99\u2e9b-\u2ef3\u2f00-\u2fd5\u2ff0-\u2ffb\u3000-\u3029\u3030\u3033-\u3036\u3038-\u303e\u3041-\u3096\u3099-\u30ff\u3105-\u3129\u3131-\u318e\u3190-\u319f\u31c0-\u31cf\u31f0-\u321c\u3220-\u324f\u3251-\u327b\u327f-\u32cb\u32d0-\u332b\u332d-\u3371\u337b-\u33d8\u33da-\u33dd\u33e0-\u33fe\u3400-\u4db5\u4dc0-\u9fc2\u9fc4\u9fc6-\u9fd0\ua000-\ua48c\ua490-\ua4c6\ua4d0-\ua62b\ua640-\ua69d\ua69f-\ua6f7\ua700-\ua721\ua727\ua730-\ua731\ua789-\ua78c\ua792\ua7a4\ua800-\ua82b\ua830-\ua839\ua840-\ua877\ua880-\ua8c4\ua8ce-\ua8d9\ua900-\ua953\ua95f\ua980-\ua9cd\ua9cf-\ua9d9\ua9de-\ua9fe\uaa00-\uaa36\uaa40-\uaa4d\uaa50-\uaa59\uaa5c-\uaac2\uaadb-\uaaf6\uab01-\uab06\uab09-\uab0e\uab11-\uab16\uab20-\uab26\uab28-\uab2e\uab53\uab70-\uabed\uabf0-\uabf9\uac00-\ud7a3\ue000\uf6c3\uf900-\ufa2d\ufa30-\ufa6d\ufb00-\ufb06\ufb13-\ufb17\ufb1d-\ufb36\ufb38-\ufb3c\ufb3e\ufb40-\ufb41\ufb43-\ufb44\ufb46-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd92-\ufdc7\ufdf0-\ufdfd\ufe00\ufe10-\ufe19\ufe20-\ufe2d\ufe30-\ufe52\ufe54-\ufe66\ufe68-\ufe6b\ufe70-\ufe74\ufe76-\ufefc\ufeff\uff01-\uff9f\uffa1\uffa4\uffa7\uffe0-\uffe6\uffe8-\uffee\ufffc-\ufffd\U00010000-\U0001000b\U0001000d-\U00010026\U00010028-\U0001003a\U0001003c-\U0001003d\U0001003f-\U0001004d\U00010050-\U0001005d\U00010080-\U000100fa\U00010100-\U00010102\U00010107-\U00010133\U00010137-\U00010143\U00010146-\U00010175\U00010179-\U00010182\U00010184-\U00010186\U0001018a\U00010280-\U0001029c\U000102a0-\U000102d0\U00010300-\U0001031e\U00010320-\U00010323\U00010330-\U0001034a\U00010350-\U0001037a\U00010380-\U0001039d\U0001039f-\U000103c3\U000103c8-\U000103d5\U00010400-\U0001049d\U000104a0-\U000104a9\U000104b0-\U000104d3\U000104d8-\U000104fb\U00010500-\U00010527\U00010600-\U00010736\U00010740-\U00010755\U00010760-\U00010767\U00010800-\U00010805\U00010808\U0001080a-\U00010835\U00010837-\U00010838\U0001083c\U0001083f-\U00010855\U00010857-\U0001089e\U000108a7-\U000108af\U000108e0-\U000108f2\U000108f4-\U000108f5\U000108fb-\U0001091b\U0001091f-\U00010939\U0001093f\U00010980-\U000109b7\U000109bc-\U000109cf\U000109d2-\U00010a03\U00010a05-\U00010a06\U00010a0c-\U00010a13\U00010a15-\U00010a17\U00010a19-\U00010a33\U00010a38-\U00010a3a\U00010a3f-\U00010a47\U00010a50-\U00010a58\U00010a60-\U00010a9f\U00010ac0-\U00010ae6\U00010aeb-\U00010af6\U00010b00-\U00010b35\U00010b39-\U00010b55\U00010b58-\U00010b72\U00010b78-\U00010b7f\U00010c00-\U00010c48\U00010d00-\U00010d27\U00010d30-\U00010d39\U00011000-\U0001104d\U00011052-\U0001106f\U00011080-\U000110c1\U000110d0-\U000110e8\U000110f0-\U000110f9\U00011100-\U00011134\U00011136-\U00011146\U00011180-\U000111cd\U000111d0-\U000111df\U00011200-\U00011211\U00011213-\U0001123e\U00011280-\U00011286\U00011288\U0001128a-\U0001128d\U0001128f-\U0001129d\U0001129f-\U000112a9\U00011300-\U00011303\U00011305-\U0001130c\U0001130f-\U00011310\U00011313-\U00011328\U0001132a-\U00011330\U00011332-\U00011333\U00011335-\U00011339\U0001133b-\U00011344\U00011347-\U00011348\U0001134b-\U0001134d\U00011350\U00011357\U0001135d-\U00011363\U00011366-\U0001136c\U00011370-\U00011374\U00011400-\U00011459\U0001145b\U0001145d\U00011600-\U00011644\U00011650-\U00011659\U00011680-\U000116b8\U000116c0-\U000116c9\U00011700-\U00011719\U0001171d-\U0001172b\U00011730-\U0001173f\U000118a0-\U000118f2\U000118ff\U00011ac0-\U00011af8\U00011c00-\U00011c08\U00011c0a-\U00011c36\U00011c38-\U00011c45\U00011c50-\U00011c6c\U00011c70-\U00011c8f\U00011c92-\U00011ca7\U00011ca9-\U00011cb6\U00011d00-\U00011d06\U00011d08-\U00011d09\U00011d0b-\U00011d36\U00011d3a\U00011d3c-\U00011d3d\U00011d3f-\U00011d47\U00011d50-\U00011d59\U00011d60-\U00011d65\U00011d67-\U00011d68\U00011d6a-\U00011d8e\U00011d90-\U00011d91\U00011d93-\U00011d98\U00011da0-\U00011da9\U00012000-\U0001236e\U00012400-\U00012462\U00012470-\U00012473\U00013000-\U0001342e\U00016800-\U00016a38\U00016a40-\U00016a5e\U00016a60-\U00016a69\U00016a6e-\U00016a6f\U00016ad0-\U00016aed\U00016af0-\U00016af5\U00016b00-\U00016b45\U00016b50-\U00016b59\U00016b5b-\U00016b61\U00016b63-\U00016b77\U00016b7d-\U00016b8f\U00016f00-\U00016f44\U00016f50-\U00016f7e\U00016f8f-\U00016f9f\U0001d100-\U0001d108\U0001d110-\U0001d112\U0001d11e\U0001d121-\U0001d122\U0001d12a-\U0001d12b\U0001d192-\U0001d193\U0001d1a6-\U0001d1a8\U0001d1c7-\U0001d1ce\U0001d300-\U0001d356\U0001d360-\U0001d371\U0001d400-\U0001d454\U0001d456-\U0001d49c\U0001d49e-\U0001d49f\U0001d4a2\U0001d4a5-\U0001d4a6\U0001d4a9-\U0001d4ac\U0001d4ae-\U0001d4b9\U0001d4bb\U0001d4bd-\U0001d4c3\U0001d4c5-\U0001d505\U0001d507-\U0001d50a\U0001d50d-\U0001d514\U0001d516-\U0001d51c\U0001d51e-\U0001d539\U0001d53b-\U0001d53e\U0001d540-\U0001d544\U0001d546\U0001d54a-\U0001d550\U0001d552-\U0001d6a5\U0001d6a8-\U0001d7c9\U0001d7ce-\U0001d7ff\U0001e2c0-\U0001e2f9\U0001e2ff\U0001e900-\U0001e94b\U0001e950-\U0001e959\U0001e95e-\U0001e95f\U0001f000-\U0001f02b\U0001f030-\U0001f093\U0001f0a0-\U0001f0ae\U0001f0b1-\U0001f0be\U0001f0c1-\U0001f0cf\U0001f0d1-\U0001f0df\U0001f100-\U0001f10c\U0001f110-\U0001f129\U0001f130-\U0001f149\U0001f14f-\U0001f16b\U0001f170-\U0001f189\U0001f18e-\U0001f18f\U0001f191-\U0001f19a\U0001f1e6-\U0001f1ff\U0001f201-\U0001f202\U0001f210-\U0001f212\U0001f215-\U0001f23a\U0001f240-\U0001f248\U0001f250-\U0001f251\U0001f300-\U0001f321\U0001f324-\U0001f393\U0001f396-\U0001f397\U0001f399-\U0001f39b\U0001f39e-\U0001f3f0\U0001f3f3-\U0001f3f5\U0001f3f7-\U0001f4fd\U0001f4ff-\U0001f53d\U0001f549-\U0001f54e\U0001f550-\U0001f567\U0001f56f-\U0001f570\U0001f573-\U0001f57a\U0001f587\U0001f58a-\U0001f58d\U0001f590\U0001f595-\U0001f596\U0001f5a4-\U0001f5a5\U0001f5a8\U0001f5b1-\U0001f5b2\U0001f5bc\U0001f5c2-\U0001f5c4\U0001f5d1-\U0001f5d3\U0001f5dc-\U0001f5de\U0001f5e1\U0001f5e3\U0001f5e8\U0001f5ef\U0001f5f3\U0001f5fa-\U0001f64f\U0001f680-\U0001f6c5\U0001f6cb-\U0001f6d2\U0001f6d5-\U0001f6d7\U0001f6e0-\U0001f6e5\U0001f6e9\U0001f6eb-\U0001f6ec\U0001f6f0\U0001f6f3-\U0001f6fc\U0001f700-\U0001f773\U0001f7e0-\U0001f7eb\U0001f90c-\U0001f93a\U0001f93c-\U0001f945\U0001f947-\U0001f978\U0001f97a-\U0001f9cb\U0001f9cd-\U0001f9ff\U0001fa70-\U0001fa74\U0001fa78-\U0001fa7a\U0001fa80-\U0001fa86\U0001fa90-\U0001faa8\U0001fab0-\U0001fab6\U0001fac0-\U0001fac2\U0001fad0-\U0001fad6\U0002000b\U00020021\U0002003e\U00020046\U0002004e\U00020068\U00020086-\U00020087\U00020089-\U0002008a\U00020094\U000200a2\U000200a4\U000200b0\U000200ca-\U000200cd\U000200d1\U000200ee\U000200f5\U0002010c\U0002010e\U00020118\U00020158\U00020164\U000201a2\U000201a4\U000201a9\U000201ab\U000201c1\U000201d4\U000201f2\U00020204\U0002020c\U00020213-\U00020214\U00020239\U0002025b\U00020274-\U00020275\U00020299\U0002029e\U000202a0\U000202b7\U000202bf-\U000202c0\U000202e5\U0002030a\U00020325\U0002032b\U00020341\U00020345-\U00020347\U00020371\U0002037e-\U00020381\U000203a0\U000203a7\U000203b5\U000203c9\U000203cb\U000203f5\U000203f9\U000203fc\U00020413-\U00020414\U0002041f\U0002044a\U00020465\U00020487\U0002048e\U00020491-\U00020492\U000204a3\U000204d7\U000204fc\U000204fe\U00020509\U0002053f\U00020547\U0002058e\U000205a5\U000205b1\U000205b3\U000205c3\U000205ca\U000205d0\U000205d5-\U000205d6\U000205df-\U000205e0\U000205eb\U00020611\U00020615\U00020619-\U0002061a\U00020628\U00020630\U00020656\U00020676\U000206ec\U0002070e\U00020731\U0002074f\U00020779\U000207c8\U00020807\U0002082c\U0002083a\U00020873\U000208b9\U000208d5\U0002090e\U00020916\U00020923\U00020954\U00020979\U0002097c\U00020984\U0002099d\U000209e7\U00020a11\U00020a50\U00020a64\U00020a6f\U00020a8a\U00020ab4\U00020ac2\U00020acd\U00020ad3\U00020b0d\U00020b1d\U00020b8f\U00020b9f\U00020ba8-\U00020ba9\U00020bb7\U00020bbf\U00020bc6\U00020bcb\U00020be2\U00020beb\U00020bfb\U00020bff\U00020c0b\U00020c0d\U00020c20\U00020c34\U00020c3a-\U00020c3b\U00020c41-\U00020c43\U00020c53\U00020c65\U00020c77-\U00020c78\U00020c7c\U00020c8d\U00020c96\U00020c9c\U00020cb5\U00020cb8\U00020ccf-\U00020cd0\U00020cd3-\U00020cd6\U00020cdd\U00020ced\U00020cff\U00020d15\U00020d28\U00020d31-\U00020d32\U00020d45-\U00020d49\U00020d4c-\U00020d4e\U00020d58\U00020d6f\U00020d71\U00020d74\U00020d7c\U00020d7e-\U00020d7f\U00020d96\U00020d9c\U00020da7\U00020db2\U00020dc8\U00020de1\U00020e04\U00020e09-\U00020e0a\U00020e0d-\U00020e11\U00020e16\U00020e1d\U00020e4c\U00020e64\U00020e6d\U00020e73\U00020e75-\U00020e7b\U00020e8c\U00020e95-\U00020e96\U00020e98\U00020e9d\U00020ea2\U00020eaa-\U00020eac\U00020eb6\U00020ed7-\U00020ed8\U00020edd\U00020ef8-\U00020efb\U00020f1d\U00020f26\U00020f2d-\U00020f2e\U00020f30-\U00020f31\U00020f3b\U00020f4c\U00020f5f\U00020f64\U00020f8d\U00020f90\U00020fad\U00020fb4-\U00020fb6\U00020fbc\U00020fdf\U00020fea-\U00020fed\U00021014\U0002101d-\U0002101e\U0002104f\U0002105c\U0002106f\U00021075-\U00021078\U0002107b\U00021088\U00021096\U0002109d\U000210b4\U000210bf-\U000210c1\U000210c7-\U000210c9\U000210cf\U000210d3\U000210e4\U000210f4-\U000210f6\U0002112f\U0002113b\U0002113d\U00021145\U00021148\U0002114f\U00021180\U00021187\U000211d9\U00021201\U0002123c-\U0002123d\U0002124f\U00021255\U00021274\U0002127b-\U0002127c\U000212a8-\U000212a9\U000212b0\U000212d7\U000212e3-\U000212e4\U000212fd-\U000212fe\U00021302-\U00021305\U0002131b\U00021336\U0002133a\U00021344\U00021375-\U00021376\U0002138e\U00021398\U0002139a\U0002139c\U000213c4-\U000213c6\U000213ed\U000213fe\U00021413\U00021416\U00021424\U0002143f\U00021452\U00021454-\U00021455\U0002146d-\U0002146e\U0002148a\U00021497\U000214b6\U000214e8\U000214fd\U00021577\U00021582\U00021596\U000215d7\U0002160a\U00021613\U00021619\U0002163e\U00021647\U00021661\U00021692\U000216b4\U000216b8\U000216ba\U000216c0-\U000216c2\U000216d3\U000216d5\U000216df\U000216e6-\U000216e8\U000216fa-\U000216fc\U000216fe\U00021706\U0002170d\U00021710\U00021726\U0002173a-\U0002173c\U00021742\U00021757\U0002176c-\U00021771\U00021773-\U00021774\U000217ab\U000217b0-\U000217b5\U000217c3\U000217c7\U000217d9-\U000217dc\U000217df\U000217ef\U000217f5-\U000217f6\U000217f8-\U000217fc\U00021820\U00021828-\U0002182a\U0002182d\U00021839-\U0002183b\U00021840\U00021845\U00021852\U0002185e\U00021861-\U00021864\U00021877\U0002187b\U00021883-\U00021885\U0002189e-\U000218a2\U000218bd-\U000218bf\U000218d1\U000218d6-\U000218d9\U000218fa\U00021903-\U00021905\U00021910-\U00021912\U00021915\U0002191c\U00021922\U00021927\U0002193b\U00021944\U00021958\U0002196a\U0002197c\U00021980\U00021983\U00021988\U00021996\U000219c3\U000219db\U000219f3\U00021a1a\U00021a2d\U00021a34\U00021a45\U00021a4b\U00021a63\U00021b44\U00021bc1-\U00021bc2\U00021c2a\U00021c56\U00021c70\U00021ca2\U00021ca5\U00021cac\U00021d2d\U00021d45-\U00021d46\U00021d53\U00021d5e\U00021d62\U00021d78\U00021d90\U00021d92\U00021d9c\U00021da1\U00021db6-\U00021db7\U00021dba\U00021dca\U00021dd1\U00021de0\U00021deb\U00021df9\U00021e1c\U00021e23\U00021e33-\U00021e34\U00021e37\U00021e3d\U00021e89\U00021ea4\U00021ea8\U00021ec8\U00021ed5\U00021f0f\U00021f15\U00021f1e\U00021f6a\U00021f76\U00021f9e\U00021fa1\U00021fe8\U00021ffa\U00022045\U00022049\U0002207e\U0002209a\U000220c7\U000220fc\U0002212a\U0002215b\U00022173\U0002217a-\U0002217b\U000221a1\U000221c1\U000221c3\U00022208\U00022218\U0002227c\U0002231e\U00022321\U00022325\U000223ad\U000223bd\U000223d0\U000223d7\U000223fa\U00022465\U00022471\U0002248b\U00022491\U000224b0\U000224bc\U000224c1\U000224c9\U000224cc\U000224ed\U00022513\U0002251b\U00022530\U00022554\U0002258d\U000225af\U000225be\U00022609\U0002261b-\U0002261c\U0002262b\U00022668\U0002267a\U00022696\U00022698\U000226f3-\U000226f6\U00022712\U00022714\U0002271b\U0002271f\U0002272a\U00022775\U00022781\U00022796\U000227b4-\U000227b5\U000227cd\U00022803\U0002285b\U0002285f-\U00022860\U00022871\U000228ab\U000228ad\U000228c1\U000228f7\U00022926\U00022939\U0002294f\U00022967\U0002296b\U00022980\U0002298f\U00022993\U00022a66\U00022ab8\U00022acf\U00022ad5\U00022ae6\U00022ae8\U00022b0e\U00022b22\U00022b3f\U00022b43\U00022b46\U00022b4f-\U00022b50\U00022b6a\U00022ba6\U00022bca\U00022bce\U00022c1d\U00022c24\U00022c26-\U00022c27\U00022c38\U00022c4c\U00022c51\U00022c55\U00022c62\U00022c88\U00022c9b\U00022ca1\U00022ca9\U00022cb2\U00022cb7\U00022cc2\U00022cc6\U00022cc9\U00022d07-\U00022d08\U00022d12\U00022d44\U00022d4c\U00022d67\U00022d8d\U00022d95\U00022da0\U00022da3-\U00022da4\U00022db7\U00022de1\U00022dee\U00022e0d\U00022e36\U00022e42\U00022e78\U00022e8b\U00022eb3\U00022eef\U00022f74\U00022fcc\U00022fe3\U00022feb\U00023033\U00023044\U0002304b\U00023066\U0002307d-\U0002307e\U0002308e\U000230b7\U000230bc\U000230da\U00023103\U0002313d\U0002317d\U00023182\U000231a4-\U000231a5\U000231b3\U000231b6\U000231c3-\U000231c4\U000231c8-\U000231c9\U000231ea\U000231f5\U000231f7-\U000231f9\U0002320f\U00023225\U0002322f\U00023231-\U00023234\U00023256\U0002325e\U00023262\U00023281\U00023289-\U0002328a\U000232ab-\U000232ad\U000232d2\U000232e0-\U000232e1\U00023300\U0002330a\U0002331f\U00023372\U000233b4\U000233cc\U000233d0\U000233d2-\U000233d3\U000233d5\U000233da\U000233de-\U000233df\U000233e4\U000233e6\U000233f4-\U000233f5\U000233f9-\U000233fa\U000233fe\U00023400\U0002343f\U0002344a-\U0002344b\U00023450-\U00023451\U00023465\U0002346f\U00023472\U000234e4-\U000234e5\U00023519\U00023530\U00023551\U0002355a\U00023567\U00023594-\U00023595\U00023599\U0002359c\U000235bb\U000235c4\U000235cb\U000235cd-\U000235cf\U000235f3\U00023600\U00023617\U0002361a\U00023638-\U0002363a\U0002363c\U00023640\U00023647\U00023659\U0002365f\U00023677\U0002368e\U0002369e\U000236a6\U000236ad\U000236ba\U000236df\U000236ee\U00023703\U0002370c\U00023716\U0002371c\U00023720\U0002372d\U0002372f\U0002373f\U00023763-\U00023764\U00023766\U00023781\U000237a2\U000237bc\U000237c2\U000237d5-\U000237d7\U000237e7\U000237f1\U000237ff\U00023824\U0002383a\U0002383d\U000239c2\U00023a98\U00023aa7\U00023adb\U00023aee\U00023afa\U00023b1a\U00023b5a\U00023c63\U00023c7f\U00023c97-\U00023c9b\U00023cb5\U00023cb7\U00023cbe\U00023cc7-\U00023cc9\U00023cfc-\U00023d00\U00023d0e\U00023d40\U00023d5b\U00023d7e\U00023d8f\U00023db6-\U00023dbd\U00023dd3\U00023de3\U00023df8-\U00023dfa\U00023e06\U00023e11\U00023e23\U00023e2c-\U00023e31\U00023e39\U00023e88-\U00023e8b\U00023eb9\U00023ebf\U00023ed7\U00023ef7-\U00023efc\U00023f35\U00023f41\U00023f4a\U00023f61\U00023f7e-\U00023f82\U00023f8f\U00023fb4\U00023fb7\U00023fc0\U00023fc5\U00023feb-\U00023ff0\U00024011\U00024039-\U0002403d\U0002404b\U00024057\U00024085\U0002408b-\U0002408d\U00024091\U00024096\U000240c9\U000240e1\U000240ec\U00024103-\U00024104\U0002410f\U00024119\U0002413f-\U00024140\U00024144\U0002414e\U00024155-\U00024157\U0002415c\U0002415f\U00024161\U00024177\U0002417a\U000241a3-\U000241a5\U000241ac\U000241b5\U000241c6\U000241cd\U000241e2\U000241fc\U000241fe\U0002421b\U0002424b\U00024256\U00024259\U00024276-\U00024278\U00024284\U00024293\U00024295\U000242a5\U000242bf\U000242c1\U000242c9-\U000242ca\U000242ee\U000242fa\U0002430d\U0002431a\U00024334\U00024348\U00024362-\U00024365\U0002438c\U00024396\U0002439c\U000243bc-\U000243bd\U000243c1\U000243d0\U000243e9-\U000243ea\U000243f2\U000243f8\U00024404\U00024435-\U00024436\U0002445a-\U0002445b\U00024473\U00024487-\U00024488\U000244b9\U000244bc\U000244ce\U000244d3\U000244d6\U00024505\U00024521\U00024578\U000245c8\U00024618\U00024629-\U0002462a\U00024665\U00024674\U00024697\U000246a5\U000246d4\U00024706\U00024725\U0002472f\U0002478f\U000247e0\U000247f1\U00024812\U00024823\U00024882\U00024896\U000248e9\U000248f0-\U000248f3\U000248fb\U000248ff-\U00024901\U0002490c\U00024916-\U00024917\U00024919\U0002492f\U00024933-\U00024934\U0002493e-\U00024943\U00024962-\U00024963\U00024974-\U00024976\U0002497b\U0002497f\U00024982\U00024988-\U0002498f\U00024994\U000249a4\U000249a7\U000249a9\U000249ab-\U000249ad\U000249b7-\U000249bb\U000249c5\U000249d0\U000249da-\U000249db\U000249de-\U000249df\U000249e3\U000249e5\U000249ec-\U000249ed\U000249f6-\U000249f9\U000249fb\U00024a0e\U00024a12-\U00024a13\U00024a15\U00024a21-\U00024a2a\U00024a3e\U00024a42\U00024a45\U00024a4a\U00024a4d-\U00024a51\U00024a5d\U00024a65-\U00024a67\U00024a71\U00024a77-\U00024a7a\U00024a7d\U00024a8c\U00024a93-\U00024a96\U00024aa4-\U00024aa7\U00024ab1-\U00024ab3\U00024aba-\U00024abc\U00024ac0\U00024ac7\U00024ac9-\U00024aca\U00024ad1\U00024adf\U00024ae2\U00024ae9\U00024b0f\U00024b56\U00024b6e-\U00024b6f\U00024bf5\U00024c09\U00024c16\U00024c9e-\U00024c9f\U00024cc9\U00024cd9\U00024d06\U00024d13-\U00024d14\U00024db8\U00024dea-\U00024deb\U00024e04\U00024e0e\U00024e37\U00024e3b\U00024e50\U00024e6a\U00024e8b\U00024ea5\U00024ea7\U00024f0e\U00024f5c\U00024f82\U00024f86\U00024f97\U00024f9a\U00024fa9\U00024fb8\U00024fc2\U00024ff2\U0002502c\U0002504a\U00025052\U00025055\U0002509d\U00025122\U0002512b\U00025148\U0002517d-\U0002517e\U000251a9\U000251cd\U000251e3\U000251e5-\U000251e7\U0002521e\U00025220-\U00025221\U0002524c\U00025250\U00025299\U000252c7\U000252d8\U0002530e\U00025311\U00025313\U00025419\U00025425\U0002542e-\U00025430\U00025446\U0002546c\U0002546e\U0002548e\U0002549a\U000254d9\U0002550e\U00025531-\U00025532\U00025535\U0002553f\U0002555b-\U0002555e\U00025562\U00025565-\U00025566\U00025581\U00025584\U0002558f\U000255a7-\U000255a8\U000255b9\U000255d5\U000255db\U000255e0\U00025605\U00025635\U00025651\U0002567f\U00025683\U00025695\U000256e3\U000256f6\U00025706\U0002571d\U00025725\U0002573d\U00025771-\U00025772\U000257a9\U000257b4\U000257c7\U000257df-\U000257e1\U00025857\U0002585d\U00025872\U00025874\U000258c8\U000258de\U000258e1\U00025903\U00025946\U00025956\U000259ac\U000259c4\U000259cc\U000259d4\U00025a54\U00025a95\U00025a9c\U00025aae-\U00025aaf\U00025ad7\U00025ae3-\U00025ae4\U00025ae9\U00025af1\U00025b74\U00025b89\U00025bb2-\U00025bb4\U00025bc6\U00025be4\U00025be8\U00025c01\U00025c06\U00025c21\U00025c4a-\U00025c4b\U00025c64-\U00025c65\U00025c91\U00025ca4\U00025cc0-\U00025cc1\U00025cfe\U00025d20\U00025d30\U00025d43\U00025d99\U00025da1\U00025db9\U00025e0e\U00025e2e\U00025e49\U00025e56\U00025e62\U00025e65\U00025e81-\U00025e83\U00025ea6\U00025ebc\U00025ec2\U00025ed7-\U00025ed8\U00025ee8\U00025f1a\U00025f23\U00025f4b\U00025f5c\U00025fd4\U00025fe0-\U00025fe2\U00025ffb\U0002600c\U00026017\U00026021\U00026029\U00026048\U00026060\U00026064\U00026083\U00026097\U000260a4-\U000260a5\U000260ed\U00026102\U00026121\U00026159-\U0002615c\U000261ad-\U000261ae\U000261b2\U000261dd\U00026221-\U00026222\U00026258\U00026261\U0002626a-\U0002626b\U00026270\U00026286\U000262d0\U00026335\U0002634b-\U0002634c\U00026351\U000263be\U000263f5\U000263f8\U00026402\U00026410-\U00026412\U0002644a\U00026469\U00026484\U00026488-\U00026489\U0002648d\U00026498\U00026512\U00026572\U000265a0\U000265ad\U000265bf\U00026612\U00026626\U00026676\U0002667e\U000266af-\U000266b1\U000266b5\U000266da\U000266e8\U000266fc\U00026716\U0002671d\U00026741\U0002677c\U00026799\U000267b3-\U000267b4\U000267cc\U0002681c\U00026846\U0002685e\U0002686e\U00026888\U0002688a\U00026893\U000268c7\U000268dd\U000268ea\U0002690e\U00026911\U00026926\U00026939\U00026951\U0002696f\U00026999\U000269a8\U000269b5\U000269dd\U000269f2\U000269fa\U00026a1e\U00026a2d-\U00026a2e\U00026a34\U00026a42\U00026a51-\U00026a52\U00026a58\U00026a8c\U00026ab7\U00026aff\U00026b05\U00026b0a\U00026b13\U00026b15\U00026b23\U00026b28\U00026b50-\U00026b53\U00026b5b-\U00026b5c\U00026b75\U00026b82\U00026b96-\U00026b97\U00026b9d\U00026bb3\U00026bc0\U00026bf7\U00026c21\U00026c29\U00026c40-\U00026c41\U00026c46\U00026c73\U00026c7e-\U00026c82\U00026c9e\U00026ca4\U00026cb7-\U00026cb8\U00026cbd\U00026cc0\U00026cc3\U00026cd1\U00026cdd\U00026d22-\U00026d2a\U00026d51\U00026d74\U00026da0-\U00026da7\U00026dae\U00026ddc\U00026dea-\U00026deb\U00026df0\U00026e00\U00026e05\U00026e07\U00026e12\U00026e40\U00026e42-\U00026e45\U00026e65\U00026e6e\U00026e72\U00026e77\U00026e84\U00026e88\U00026e8b\U00026e99\U00026ed0-\U00026ed7\U00026f26\U00026f73-\U00026f74\U00026f94\U00026f9f\U00026fa1\U00026fbe\U00026fde-\U00026fdf\U00026ff6-\U00026ff8\U0002700e\U0002704b\U00027052-\U00027053\U00027088\U000270ad-\U000270af\U000270cd\U000270d2\U000270f0\U000270f4\U000270f8\U00027109\U0002710c-\U0002710d\U00027126-\U00027127\U00027139\U00027164-\U00027165\U00027175\U000271cd\U0002721b\U00027267\U00027280\U00027285\U0002728b\U000272b2\U000272b6\U000272e6\U00027352\U0002739a\U000273da-\U000273db\U000273fe-\U000273ff\U00027410\U00027422\U00027449\U00027450\U00027484\U00027486\U000274bd\U00027574\U000275a3\U000275e0\U000275e4\U000275fd-\U000275fe\U00027607\U0002760c\U00027614-\U00027615\U00027631-\U00027632\U00027639\U00027655-\U00027657\U00027684\U00027693-\U00027694\U0002770e-\U0002770f\U00027723\U00027735-\U00027736\U00027741\U00027752\U0002775e\U00027784-\U00027785\U000277cc\U00027858\U00027870\U0002789d\U000278b2\U000278c8\U00027924\U00027967\U0002797a\U00027985\U000279a0\U000279b4\U000279dd\U000279fd\U00027a0a\U00027a0e\U00027a3e\U00027a53\U00027a59\U00027a79\U00027a84\U00027abd-\U00027abe\U00027af4\U00027b06\U00027b0b\U00027b18\U00027b38-\U00027b3a\U00027b48\U00027b65\U00027bb3\U00027bbe\U00027bc7\U00027bef\U00027bf4\U00027c12\U00027c3c\U00027c6c\U00027cb1\U00027cb8\U00027cc5\U00027d2f\U00027d53-\U00027d54\U00027d66\U00027d73\U00027d84\U00027d8f\U00027d98\U00027da0\U00027dbd\U00027ddc\U00027e10\U00027e4d\U00027e4f\U00027f2e\U00027fb7\U00027ff9\U00028002\U00028009\U0002801e\U00028023-\U00028024\U00028048\U00028083\U0002808a\U00028090\U000280bb\U000280bd-\U000280be\U000280e8-\U000280e9\U000280f4\U0002812e\U0002814f\U0002815d\U0002816f\U00028189\U000281af\U000281bc\U00028207\U00028218\U0002821a\U00028256\U00028277\U0002827c\U00028282\U0002829b\U000282cd\U000282e2\U000282f3\U00028306\U00028318\U0002832f\U0002833a\U00028365\U0002836d\U0002837d\U0002838a\U000283cd\U00028408\U0002840c\U00028412\U00028455\U00028468\U0002846c\U00028473\U00028482\U00028501\U0002853c-\U0002853d\U0002856b-\U0002856c\U000285c8-\U000285c9\U000285e8\U000285f4\U00028600\U0002860b\U00028625\U0002863b\U00028678\U00028695\U000286aa-\U000286ab\U000286b2\U000286bc\U000286d7-\U000286d8\U000286e6\U000286fa\U0002870f\U00028713\U000287e0\U00028804\U0002882b\U0002890d\U00028933\U00028946\U00028948-\U00028949\U00028956\U00028964\U00028968\U0002896b-\U0002896d\U0002897e\U00028987-\U00028989\U000289a8\U000289aa-\U000289ab\U000289b8\U000289ba-\U000289bc\U000289c0\U000289dc\U000289de\U000289e1\U000289e3-\U000289e4\U000289e7-\U000289e8\U000289f9-\U000289fc\U00028a0f\U00028a16\U00028a1e\U00028a25\U00028a29\U00028a32\U00028a36\U00028a43-\U00028a4b\U00028a59-\U00028a5a\U00028a71\U00028a81-\U00028a83\U00028a99-\U00028a9c\U00028ac0\U00028ac6\U00028acb-\U00028ace\U00028add-\U00028ae5\U00028aea\U00028afc\U00028b0c\U00028b13\U00028b21-\U00028b22\U00028b2b-\U00028b2d\U00028b2f\U00028b46\U00028b49\U00028b4c\U00028b4e\U00028b50\U00028b63-\U00028b66\U00028b6c\U00028b8f\U00028b99\U00028b9c-\U00028b9d\U00028bb9\U00028bc1-\U00028bc2\U00028bc5\U00028bd4\U00028bd7\U00028bd9-\U00028bda\U00028be7-\U00028bec\U00028bef\U00028bf5\U00028bff\U00028c03\U00028c09\U00028c1c-\U00028c1d\U00028c23\U00028c26\U00028c2b\U00028c30\U00028c39\U00028c3b\U00028c47\U00028c4f\U00028c51\U00028c54\U00028cca\U00028ccd\U00028cd2\U00028cdd\U00028d10\U00028d34\U00028d71\U00028d99\U00028db9\U00028dfb\U00028e0f\U00028e17\U00028e1f\U00028e36\U00028e39\U00028e65-\U00028e66\U00028e89\U00028e97\U00028e99\U00028eac\U00028eb2-\U00028eb3\U00028ed9\U00028ee7\U00028eeb\U00028ef6\U00028f32\U00028fc5\U00028ff8\U00029079\U00029088\U0002908b\U00029093\U000290af-\U000290b1\U000290c0\U000290e4-\U000290e5\U000290ec-\U000290ed\U0002910d\U00029110\U0002913c\U0002914d\U0002915b\U0002915e\U00029170\U0002919c\U000291a8\U000291d5\U000291eb\U000292a0\U000292b1\U0002941d\U00029420\U00029433\U0002943f\U00029448\U00029490\U000294d0\U000294d9-\U000294da\U000294e5\U000294e7\U0002959e\U000295b0\U000295b8\U000295cf\U000295d7\U000295e9\U000295f4\U0002967f\U000296f0\U00029719\U00029720\U00029732\U00029750\U000297d4\U00029810\U00029857\U000298a4\U000298c6\U000298d1\U000298ea\U000298f1\U000298fa\U00029903\U00029905\U0002992f\U00029945\U00029947-\U00029949\U0002995d\U0002996a\U0002999d\U000299c3\U000299c9\U00029a28\U00029a4d\U00029a72\U00029b05\U00029b0e\U00029bd5\U00029c73\U00029cad\U00029d3e\U00029d4b\U00029d5a\U00029d7c\U00029d98\U00029d9b\U00029ddb\U00029df6\U00029e06\U00029e15\U00029e2d\U00029e3d\U00029e49\U00029e68\U00029e8a\U00029eac\U00029eb0\U00029ec3-\U00029ec4\U00029edb\U00029ee9\U00029ef8\U00029f23\U00029f30\U00029f7e\U00029f83\U00029f8c\U00029fb7\U00029fce\U00029fd7\U00029fde\U0002a014\U0002a01a\U0002a02f\U0002a082\U0002a087\U0002a0b9\U0002a0e1\U0002a0ed\U0002a0f3\U0002a0f8-\U0002a0f9\U0002a0fe\U0002a107\U0002a123\U0002a133-\U0002a134\U0002a150\U0002a190\U0002a192-\U0002a193\U0002a1ab\U0002a1b4-\U0002a1b5\U0002a1df\U0002a1f5\U0002a220\U0002a233\U0002a293\U0002a29f\U0002a2b2\U0002a2b4\U0002a2b6\U0002a2ba\U0002a2bd\U0002a2df\U0002a2ff\U0002a351\U0002a38c\U0002a3a9\U0002a3ed\U0002a434\U0002a437\U0002a45b\U0002a5c6\U0002a5cb\U0002a5f1\U0002a601-\U0002a602\U0002a61a\U0002a632\U0002a64a\U0002a65b\U0002a6a9\U0002a6b2\U0002a7dd\U0002a8fb\U0002a917\U0002a9e6\U0002aa30\U0002aa36\U0002aa58\U0002adff\U0002afa2\U0002b127-\U0002b128\U0002b137-\U0002b138\U0002b1ed\U0002b300\U0002b363\U0002b36f\U0002b372\U0002b37d\U0002b404\U0002b410\U0002b413\U0002b461\U0002b4e7\U0002b4ef\U0002b4f6\U0002b4f9\U0002b50d-\U0002b50e\U0002b536\U0002b5ae-\U0002b5af\U0002b5b3\U0002b5e7\U0002b5f4\U0002b61c-\U0002b61d\U0002b626-\U0002b628\U0002b62a\U0002b62c\U0002b695-\U0002b696\U0002b6ad\U0002b6ed\U0002b746\U0002b751\U0002b753\U0002b75a\U0002b75c\U0002b765\U0002b776-\U0002b777\U0002b77c\U0002b782\U0002b789\U0002b78b\U0002b78e\U0002b794\U0002b7a9\U0002b7ac\U0002b7af\U0002b7bd\U0002b7c5\U0002b7c9\U0002b7cf\U0002b7d2\U0002b7d8\U0002b7e6\U0002b7f0\U0002b7f9\U0002b7fc\U0002b806\U0002b80a\U0002b80d\U0002b817\U0002b81a\U0002b81c\U0002b8b8\U0002bac7\U0002bb5f\U0002bb62\U0002bb7c\U0002bb83\U0002bc1b\U0002bd77\U0002bd87\U0002bdf7\U0002be29\U0002c029-\U0002c02a\U0002c0a9\U0002c0ca\U0002c1d5\U0002c1d9\U0002c1f9\U0002c27c\U0002c288\U0002c2a4\U0002c317\U0002c35b\U0002c361\U0002c364\U0002c488\U0002c494\U0002c497\U0002c542\U0002c613\U0002c618\U0002c621\U0002c629\U0002c62b-\U0002c62d\U0002c62f\U0002c642\U0002c64a-\U0002c64b\U0002c72c\U0002c72f\U0002c79f\U0002c7c1\U0002c7fd\U0002c8d9\U0002c8de\U0002c8e1\U0002c8f3\U0002c907\U0002c90a\U0002c91d\U0002ca02\U0002ca0e\U0002ca7d\U0002caa9\U0002cb29\U0002cb2d-\U0002cb2e\U0002cb31\U0002cb38-\U0002cb39\U0002cb3b\U0002cb3f\U0002cb41\U0002cb4a\U0002cb4e\U0002cb5a-\U0002cb5b\U0002cb64\U0002cb69\U0002cb6c\U0002cb6f\U0002cb73\U0002cb76\U0002cb78\U0002cb7c\U0002cbb1\U0002cbbf-\U0002cbc0\U0002cbce\U0002cc56\U0002cc5f\U0002ccf5-\U0002ccf6\U0002ccfd\U0002ccff\U0002cd02-\U0002cd03\U0002cd0a\U0002cd8b\U0002cd8d\U0002cd8f-\U0002cd90\U0002cd9f-\U0002cda0\U0002cda8\U0002cdad-\U0002cdae\U0002cdd5\U0002ce18\U0002ce1a\U0002ce23\U0002ce26\U0002ce2a\U0002ce7c\U0002ce88\U0002ce93\U0002d544\U0002e278\U0002e569\U0002e6ea\U0002f804\U0002f80f\U0002f815\U0002f818\U0002f81a\U0002f822\U0002f825\U0002f828\U0002f82c\U0002f833\U0002f83b\U0002f83f-\U0002f840\U0002f846\U0002f852\U0002f862\U0002f86d\U0002f873\U0002f877-\U0002f878\U0002f884\U0002f894\U0002f899-\U0002f89a\U0002f8a6\U0002f8ac\U0002f8b2\U0002f8b6\U0002f8cd\U0002f8d3\U0002f8db-\U0002f8dc\U0002f8e1\U0002f8e5\U0002f8ea\U0002f8ed\U0002f8fc\U0002f903\U0002f90b\U0002f90f\U0002f91a\U0002f920-\U0002f921\U0002f945\U0002f947\U0002f96c\U0002f994-\U0002f995\U0002f9b2\U0002f9bc\U0002f9d0\U0002f9d4\U0002f9de-\U0002f9df\U0002f9f4\U000e0061-\U000e007a\U000e007f]')

joyo = (
    u'亜哀愛悪握圧扱安暗案以位依偉囲委威尉意慰易為異移維緯胃衣違遺医井域育'
    u'一壱逸稲芋印員因姻引飲院陰隠韻右宇羽雨渦浦運雲営影映栄永泳英衛詠鋭液疫'
    u'益駅悦謁越閲円園宴延援沿演炎煙猿縁遠鉛塩汚凹央奥往応押横欧殴王翁黄沖億'
    u'屋憶乙卸恩温穏音下化仮何価佳加可夏嫁家寡科暇果架歌河火禍稼箇花荷華菓課'
    u'貨過蚊我画芽賀雅餓介会解回塊壊快怪悔懐戒拐改械海灰界皆絵開階貝劾外害慨'
    u'概涯街該垣嚇各拡格核殻獲確穫覚角較郭閣隔革学岳楽額掛潟割喝括活渇滑褐轄'
    u'且株刈乾冠寒刊勘勧巻喚堪完官寛干幹患感慣憾換敢棺款歓汗漢環甘監看管簡緩'
    u'缶肝艦観貫還鑑間閑関陥館丸含岸眼岩頑顔願企危喜器基奇寄岐希幾忌揮机旗既'
    u'期棋棄機帰気汽祈季紀規記貴起軌輝飢騎鬼偽儀宜戯技擬欺犠疑義議菊吉喫詰却'
    u'客脚虐逆丘久休及吸宮弓急救朽求泣球究窮級糾給旧牛去居巨拒拠挙虚許距漁魚'
    u'享京供競共凶協叫境峡強恐恭挟教橋況狂狭矯胸脅興郷鏡響驚仰凝暁業局曲極玉'
    u'勤均斤琴禁筋緊菌襟謹近金吟銀九句区苦駆具愚虞空偶遇隅屈掘靴繰桑勲君薫訓'
    u'群軍郡係傾刑兄啓型契形径恵慶憩掲携敬景渓系経継茎蛍計警軽鶏芸迎鯨劇撃激'
    u'傑欠決潔穴結血月件倹健兼券剣圏堅嫌建憲懸検権犬献研絹県肩見謙賢軒遣険顕'
    u'験元原厳幻弦減源玄現言限個古呼固孤己庫弧戸故枯湖誇雇顧鼓五互午呉娯後御'
    u'悟碁語誤護交侯候光公功効厚口向后坑好孔孝工巧幸広康恒慌抗拘控攻更校構江'
    u'洪港溝甲皇硬稿紅絞綱耕考肯航荒行衡講貢購郊酵鉱鋼降項香高剛号合拷豪克刻'
    u'告国穀酷黒獄腰骨込今困墾婚恨懇昆根混紺魂佐唆左差査砂詐鎖座債催再最妻宰'
    u'彩才採栽歳済災砕祭斎細菜裁載際剤在材罪財坂咲崎作削搾昨策索錯桜冊刷察撮'
    u'擦札殺雑皿三傘参山惨散桟産算蚕賛酸暫残仕伺使刺司史嗣四士始姉姿子市師志'
    u'思指支施旨枝止死氏祉私糸紙紫肢脂至視詞詩試誌諮資賜雌飼歯事似侍児字寺慈'
    u'持時次滋治璽磁示耳自辞式識軸七執失室湿漆疾質実芝舎写射捨赦斜煮社者謝車'
    u'遮蛇邪借尺爵酌釈若寂弱主取守手朱殊狩珠種趣酒首儒受寿授樹需囚収周宗就州'
    u'修愁拾秀秋終習臭舟衆襲週酬集醜住充十従柔汁渋獣縦重銃叔宿淑祝縮粛塾熟出'
    u'術述俊春瞬准循旬殉準潤盾純巡遵順処初所暑庶緒署書諸助叙女序徐除傷償勝匠'
    u'升召商唱奨宵将小少尚床彰承抄招掌昇昭晶松沼消渉焼焦照症省硝礁祥称章笑粧'
    u'紹肖衝訟証詔詳象賞鐘障上丈乗冗剰城場壌嬢常情条浄状畳蒸譲醸錠嘱飾植殖織'
    u'職色触食辱伸信侵唇娠寝審心慎振新森浸深申真神紳臣薪親診身辛進針震人仁刃'
    u'尋甚尽迅陣酢図吹垂帥推水炊睡粋衰遂酔随髄崇数枢据杉澄寸世瀬畝是制勢姓征'
    u'性成政整星晴正清牲生盛精聖声製西誠誓請逝青静斉税隻席惜斥昔析石積籍績責'
    u'赤跡切拙接摂折設窃節説雪絶舌仙先千占宣専川戦扇栓泉浅洗染潜旋線繊船薦践'
    u'選遷銭鮮前善漸然全禅繕塑措疎礎祖租粗素組訴阻僧創双倉喪壮奏層想捜掃挿操'
    u'早曹巣槽燥争相窓総草荘葬藻装走送遭霜騒像増憎臓蔵贈造促側則即息束測足速'
    u'俗属賊族続卒存孫尊損村他多太堕妥惰打駄体対耐帯待怠態替泰滞胎袋貸退逮隊'
    u'代台大第題滝卓宅択拓沢濯託濁諾但達奪脱棚谷丹単嘆担探淡炭短端胆誕鍛団壇'
    u'弾断暖段男談値知地恥池痴稚置致遅築畜竹蓄逐秩窒茶嫡着中仲宙忠抽昼柱注虫'
    u'衷鋳駐著貯丁兆帳庁弔張彫徴懲挑朝潮町眺聴腸調超跳長頂鳥勅直朕沈珍賃鎮陳'
    u'津墜追痛通塚漬坪釣亭低停偵貞呈堤定帝底庭廷弟抵提程締艇訂逓邸泥摘敵滴的'
    u'笛適哲徹撤迭鉄典天展店添転点伝殿田電吐塗徒斗渡登途都努度土奴怒倒党冬凍'
    u'刀唐塔島悼投搭東桃棟盗湯灯当痘等答筒糖統到討謄豆踏逃透陶頭騰闘働動同堂'
    u'導洞童胴道銅峠匿得徳特督篤毒独読凸突届屯豚曇鈍内縄南軟難二尼弐肉日乳入'
    u'如尿任妊忍認寧猫熱年念燃粘悩濃納能脳農把覇波派破婆馬俳廃拝排敗杯背肺輩'
    u'配倍培媒梅買売賠陪伯博拍泊白舶薄迫漠爆縛麦箱肌畑八鉢発髪伐罰抜閥伴判半'
    u'反帆搬板版犯班畔繁般藩販範煩頒飯晩番盤蛮卑否妃彼悲扉批披比泌疲皮碑秘罷'
    u'肥被費避非飛備尾微美鼻匹必筆姫百俵標氷漂票表評描病秒苗品浜貧賓頻敏瓶不'
    u'付夫婦富布府怖扶敷普浮父符腐膚譜負賦赴附侮武舞部封風伏副復幅服福腹複覆'
    u'払沸仏物分噴墳憤奮粉紛雰文聞丙併兵塀幣平弊柄並閉陛米壁癖別偏変片編辺返'
    u'遍便勉弁保舗捕歩補穂募墓慕暮母簿倣俸包報奉宝峰崩抱放方法泡砲縫胞芳褒訪'
    u'豊邦飽乏亡傍剖坊妨帽忘忙房暴望某棒冒紡肪膨謀貿防北僕墨撲朴牧没堀奔本翻'
    u'凡盆摩磨魔麻埋妹枚毎幕膜又抹末繭万慢満漫味未魅岬密脈妙民眠務夢無矛霧婿'
    u'娘名命明盟迷銘鳴滅免綿面模茂妄毛猛盲網耗木黙目戻問紋門夜野矢厄役約薬訳'
    u'躍柳愉油癒諭輸唯優勇友幽悠憂有猶由裕誘遊郵雄融夕予余与誉預幼容庸揚揺擁'
    u'曜様洋溶用窯羊葉要謡踊陽養抑欲浴翌翼羅裸来頼雷絡落酪乱卵欄濫覧利吏履理'
    u'痢裏里離陸律率立略流留硫粒隆竜慮旅虜了僚両寮料涼猟療糧良量陵領力緑倫厘'
    u'林臨輪隣塁涙累類令例冷励礼鈴隷零霊麗齢暦歴列劣烈裂廉恋練連錬炉路露労廊'
    u'朗楼浪漏老郎六録論和話賄惑枠湾腕挨曖宛嵐畏萎椅彙茨咽淫唄鬱怨媛艶旺岡臆'
    u'俺苛牙瓦楷潰諧崖蓋骸柿顎葛釜鎌韓玩伎亀毀畿臼嗅巾僅錦惧串窟熊詣憬稽隙桁'
    u'拳鍵舷股虎錮勾梗喉乞傲駒頃痕沙挫采塞埼柵刹拶斬恣摯餌鹿𠮟嫉腫呪袖羞蹴憧'
    u'拭尻芯腎須裾凄醒脊戚煎羨腺詮箋膳狙遡曽爽痩踪捉遜汰唾堆戴誰旦綻緻酎貼嘲'
    u'捗椎爪鶴諦溺塡妬賭藤瞳栃頓貪丼那奈梨謎鍋匂虹捻罵剝箸氾汎阪斑眉膝肘訃阜'
    u'蔽餅璧蔑哺蜂貌頰睦勃昧枕蜜冥麺冶弥闇喩湧妖瘍沃拉辣藍璃慄侶瞭瑠呂賂弄籠'
    u'麓脇')
