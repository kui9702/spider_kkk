import re
import requests
import xlsxwriter
import time
import down_img
import os

global j
j = 0

def GetxxintoExcel(html):
    global count,j
    a = re.findall(r'"raw_title":"(.*?)"', html)
    b = re.findall(r'"view_price":"(.*?)"', html)
    c = re.findall(r'"item_loc":"(.*?)"', html)
    d = re.findall(r'"view_sales":"(.*?)"', html)
    e = re.findall(r'"detail_url":"(.*?)"', html)
    f = re.findall(r'"pic_url":"(.*?)"', html)
    x = []
    for i in range(len(a)):
        e[i] = 'https:'+ e[i]
        f[i] = 'https:' + f[i]
        e[i] = e[i].encode("latin-1").decode("unicode_escape")
        try:
            x.append((a[i], b[i], c[i], d[i], e[i], f[i]))
        except IndexError:
            break
    i = 0
    for i in range(len(x)):
        worksheet.set_row(j, 200)
        worksheet.write(count + i + 1, 0, x[i][0])
        worksheet.write(count + i + 1, 1, x[i][1])
        worksheet.write(count + i + 1, 2, x[i][2])
        worksheet.write(count + i + 1, 3, x[i][3])
        worksheet.write(count + i + 1, 4, x[i][4])
        worksheet.write(count + i + 1, 5, x[i][5])
        down_img.down_img(x[i][5],count + i + 1)
        path = os.path.join(r'img', str(count + i + 1) + '.jpg')
        print(path)
        worksheet.insert_image(count + i + 1, 6, path)
        j = j + 1
    count = count + len(x)
    return print("已完成")


def Geturls(q, x):
    url = "https://s.taobao.com/search?q=" + q + "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm" \
                                                 "=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306 "
    urls = []
    urls.append(url)
    if x == 1:
        return urls
    for i in range(1, x):
        url = "https://s.taobao.com/search?q=" + q + "&commend=all&ssid=s5-e&search_type=item" \
                                                     "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306" \
                                                     "&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=" + str(
            i * 44)
        urls.append(url)
    return urls


def GetHtml(url):
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r


if __name__ == "__main__":
    count = 0
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        ,
        "cookie": "hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=CM7yIxK50QpSxsDIpd0cwkPejXel5rkEStTXHo5awyT9NHAoslrHTFooEewPUiq3erf8jD8bj15JrmjhBNw9jg%3D%3D; cna=kIGuFx7Rzx8CAbcOHGuGuNZl; miid=2057412036704719215; t=99a6bc70a8d497254333dacfb5bb9825; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=145e49fd4f00e4025c81a70c5fc81fa6; _samesite_flag_=true; _uab_collina=160516517398804771947288; xlly_s=1; sgcookie=E1000ZRre5v9rDlHlwgGhj5yifUzD9AdMIp3IENtRZ90XEk1d%2BQu6WMYfwKlgpHCJseq449qJKczYYmhRclyHSAXqw%3D%3D; uc3=nk2=F5RAQpWwT9CXIsQ%3D&id2=UUphw21ta33CZ2dGog%3D%3D&vt3=F8dCufwtFxhNzT9Uhq4%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; csg=87719d05; lgc=tb505905006; dnk=tb505905006; skt=ecb71faa985544d7; existShop=MTYwNTYxMzI2Nw%3D%3D; uc4=nk4=0%40FY4L7mmwbqA8VWOk9MPb4AO5ONePlw%3D%3D&id4=0%40U2grGNI0sH6ka4CsAkfWY1oJDcRkGlte; tracknick=tb505905006; _cc_=WqG3DMC9EA%3D%3D; mt=ci=0_1; _m_h5_tk=f09dceb4ccbfb16bd76b5ab0b80bf23f_1605699623128; _m_h5_tk_enc=09b47b8d9156ab28b50ad393626d22e2; _tb_token_=e6e57dfe4eee; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=Vq8l%2BKCLiYYu&pas=0&existShop=false&cookie14=Uoe0aDqxIWCLzw%3D%3D; JSESSIONID=D29DB3B679EF6667D1F83FEC837A18F0; isg=BJSUQ56Yt_NHOyOliGMLF8ECZdIG7bjXpa-mQi51IJ-iGTRjVv2IZ0obHRGB-vAv; l=eBNOIjYeOSGjkcREBOfanurza77OSIRYYuPzaNbMiOCPOwCB5UcFWZ78CaY6C3GVh6kWR3oVpXawBeYBq7Vonxv92j-la_kmn; tfstk=csRlBofyVLWS1_6DCb1WW8HNgUGOwyPFjBRXgIPIeJtUiS5mk-yNWmucq3ALdyifu"
    }
    q = input("输入货物")
    x = int(input("你想爬取几页"))
    urls = Geturls(q, x)
    workbook = xlsxwriter.Workbook(q + ".xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 70)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 30)
    worksheet.write('A1', '名称')
    worksheet.write('B1', '价格')
    worksheet.write('C1', '地区')
    worksheet.write('D1', '付款人数')
    worksheet.write('E1', '链接')
    worksheet.write('F1', '图片地址')
    worksheet.write('G1', '图片')
    xx = []
    for url in urls:
        html = GetHtml(url)
        print(type(html))
        s = GetxxintoExcel(html.text)
        time.sleep(5)
    workbook.close()
