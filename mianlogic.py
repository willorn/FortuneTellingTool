import datetime


class Bazi:
    def __init__(self, y, m, d, h, sex):
        self.y = int(y)
        self.m = int(m) - 1
        self.d = int(d)
        self.h = int(h)
        self.sex = int(sex)

        self.tg = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.dz = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        self.dz0 = ["丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子"]
        self.jq84 = [442208451146, 444755924716, 447326679845, 449936540593, 452591457618, 455285317308,
                     458000946032, 460714673166, 463403390187, 466051355952, 468654332864, 471220083199]
        self.y_d84 = 441734400726

        self.zsss = {
            "甲": ["沐浴", "冠带", "临官", "帝旺", "衰", "病", "死", "墓", "绝", "胎", "养", "长生"],
            "乙": ["病", "衰", "帝旺", "临官", "冠带", "沐浴", "长生", "养", "胎", "绝", "墓", "死"],
            "丙": ["胎", "养", "长生", "沐浴", "冠带", "临官", "帝旺", "衰", "病", "死", "墓", "绝"],
            "丁": ["绝", "墓", "死", "病", "衰", "帝旺", "临官", "冠带", "沐浴", "长生", "养", "胎"],
            "戊": ["胎", "养", "长生", "沐浴", "冠带", "临官", "帝旺", "衰", "病", "死", "墓", "绝"],
            "己": ["绝", "墓", "死", "病", "衰", "帝旺", "临官", "冠带", "沐浴", "长生", "养", "胎"],
            "庚": ["死", "墓", "绝", "胎", "养", "长生", "沐浴", "冠带", "临官", "帝旺", "衰", "病"],
            "辛": ["长生", "养", "胎", "绝", "墓", "死", "病", "衰", "帝旺", "临官", "冠带", "沐浴"],
            "壬": ["帝旺", "衰", "病", "死", "墓", "绝", "胎", "养", "长生", "沐浴", "冠带", "临官"],
            "癸": ["临官", "冠带", "沐浴", "长生", "养", "胎", "绝", "墓", "死", "病", "衰", "帝旺"]
        }

        self.nayi = {
            "甲子": "海中金", "乙丑": "海中金", "丙寅": "炉中火", "丁卯": "炉中火",
            "戊辰": "大林木", "己巳": "大林木", "庚午": "路旁土", "辛未": "路旁土",
            "壬申": "剑锋金", "癸酉": "剑锋金", "甲戌": "山头火", "乙亥": "山头火",
            "丙子": "涧下水", "丁丑": "涧下水", "戊寅": "城墙土", "己卯": "城墙土",
            "庚辰": "白腊金", "辛巳": "白腊金", "壬午": "杨柳木", "癸未": "杨柳木",
            "甲申": "泉中水", "乙酉": "泉中水", "丙戌": "屋上土", "丁亥": "屋上土",
            "戊子": "霹雳火", "己丑": "霹雳火", "庚寅": "松柏木", "辛卯": "松柏木",
            "壬辰": "长流水", "癸巳": "长流水", "甲午": "沙中金", "乙未": "沙中金",
            "丙申": "山下火", "丁酉": "山下火", "戊戌": "平地木", "己亥": "平地木",
            "庚子": "壁上土", "辛丑": "壁上土", "壬寅": "金箔金", "癸卯": "金箔金",
            "甲辰": "覆灯火", "乙巳": "覆灯火", "丙午": "天河水", "丁未": "天河水",
            "戊申": "大驿土", "己酉": "大驿土", "庚戌": "钗钏金", "辛亥": "钗钏金",
            "壬子": "桑柘木", "癸丑": "桑柘木", "甲寅": "大溪水", "乙卯": "大溪水",
            "丙辰": "沙中土", "丁巳": "沙中土", "戊午": "天上火", "己未": "天上火",
            "庚申": "石榴木", "辛酉": "石榴木", "壬戌": "大海水", "癸亥": "大海水"
        }

    def y_gan(self):  # 年干
        return self.tg[(self.y + 6) % 10]

    def y_zhi(self):  # 年支
        if self.y - 1984 <= 0:
            nz = self.dz0[11 + (self.y - 1984) % 12]
        else:
            nz = self.dz0[(self.y - 1984) % 12 - 1]
        return nz

    def y_zhu(self):  # 年柱
        return self.y_gan() + self.y_zhi()

    def m_gan(self):  # 月干
        ng = self.y_gan()
        yg = None
        if ng in ["甲", "己"]:
            yg = self.tg[(1 + self.m) % 10]
        elif ng in ["乙", "庚"]:
            yg = self.tg[(3 + self.m) % 10]
        elif ng in ["丙", "辛"]:
            yg = self.tg[(5 + self.m) % 10]
        elif ng in ["丁", "壬"]:
            yg = self.tg[(7 + self.m) % 10]
        elif ng in ["戊", "癸"]:
            yg = self.tg[(9 + self.m) % 10]
        return yg

    def m_zhi(self):  # 月支
        return self.dz0[self.m]

    def m_zhu(self):  # 月柱
        return self.m_gan() + self.m_zhi()

    def d_gan(self):  # 日干
        y_d84 = datetime.datetime(1984, 1, 1)
        y_t = datetime.datetime(self.y, self.m + 1, self.d, self.h)
        y_r = (y_t - y_d84).days % 60
        return self.tg[y_r % 10]

    def d_zhi(self):  # 日支
        y_d84 = datetime.datetime(1984, 1, 1)
        y_t = datetime.datetime(self.y, self.m + 1, self.d, self.h)
        y_r = (y_t - y_d84).days % 60
        return self.dz0[y_r % 12]

    def d_zhu(self):  # 日柱
        return self.d_gan() + self.d_zhi()

    def h_gan(self):  # 时干
        rg = self.d_gan()
        sz = self.dz0[self.h // 2]
        if rg in ["甲", "己"]:
            return self.tg[(1 + self.h // 2) % 10]
        elif rg in ["乙", "庚"]:
            return self.tg[(3 + self.h // 2) % 10]
        elif rg in ["丙", "辛"]:
            return self.tg[(5 + self.h // 2) % 10]
        elif rg in ["丁", "壬"]:
            return self.tg[(7 + self.h // 2) % 10]
        elif rg in ["戊", "癸"]:
            return self.tg[(9 + self.h // 2) % 10]

    def h_zhi(self):  # 时支
        return self.dz0[self.h // 2]

    def h_zhu(self):  # 时柱
        return self.h_gan() + self.h_zhi()

    def da_yun(self):  # 大运
        # Assuming some logic for Da Yun calculation
        pass

    def output(self):
        print(f"年柱: {self.y_zhu()}")
        print(f"月柱: {self.m_zhu()}")
        print(f"日柱: {self.d_zhu()}")
        print(f"时柱: {self.h_zhu()}")


# todo maybe some logic error here
bazi = Bazi(1998, 9, 14, 11, 1)
bazi.output()
