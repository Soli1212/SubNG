# 𝕊𝕦𝕓ℕ𝔾 🐙
خب من سهیلم و یک api تمیز و کاربردی با پایتون براتون توسعه دادم   در واقع کار اصلی این پروژه به این صورت که هر باری که شما بهش درخواست میزنید به اکانت تلگرامتون متصل و از گروه/کانال های هدفتون کانفیگ های v2ray رو استخراج و در پاسخ بهتون برمیگردونه .🍃
 
 ⚫دقت داشته باشید اتصال و توکن ورودی به برنامه کاملا رمزنگاری میشه و امن هست.
  
 ⚫نیازی به اتصال  به vpn نیست
#
کانفیگ و راه اندازی🛠


وارد پوشه SubNG شید و فایل requirements.txt رو نصل کنید .

**دریافت api hash و api id**

در قدم اول شما باید api id و api hash اکانت تلگرام مورد نظرتون رو از [اینجا](https://my.telegram.org/)
 دریافت کنید

 

**ساخت توکن رمزنگاری شده**

1 - فایل SessionMaker.py درون پروژه رو اجرا کنید . 

2 - ورودی های مورد نیاز رو به برنامه بدید دقت کنید SessionKey رو یک کلید ایمن و خوب در نظر بگیرید و کارکتر های @ ؟ # \ / داخل اون نباشه . 
بعد از دریافت کد از تلگرام و ورود به حساب یک عبارت رمزنگاری شده با الگوریتم AES بهتون میده که به همون SessionKey رمزنگاری شده . 

3 - عبارت رمزنگاری شده که فایل SessionMaker.py بهتون داده کپی و وارد SubNG/InputData.py بشید و عبارت رمزنگاری شده رو در متغیر LoginSession به صورت String قرار بدید . 

4 - ایدی (ID) کانال یا گروه های هدف رو به رو در متغیر Channels در فایل  SubNG/InputData.py قرار بدید نمونه در خود فایل موجود است .

#
خب تا اینجا ما پروژه رو کانفیگ کردیم و آماده Deploy هستش شما میتونید روی سرور شخصی و یا هر جایی که دوست دارید پروژه رو مستقر کنید .

🟣 پیشنهاد من سایت [huggingface.co](https://huggingface.co/)
هست این سایت رایگانه. با fastapi سازگاره و از Docker پشتیبانی میکنه و سرعت نسبتا خوبی رو هتون میده
.

ادامه مراحل رو با huggingface پیش میریم

5 - خب لطفا در huggingface اگر [حسابی](https://huggingface.co/join) دارید در آن Login و اگر هم ندارید یکی بسازید فرایند ساخت حساب خیلی سادس از [TempMail](https://temp-mail.org/en/)
 هم میتونید استفاده کنید . 

6 - بعد از ساخت حساب یک Space ایجاد کنید

. حالت Public باشه و SDK اون رو Docker بزارید 

7 - بعد از ساخت space  از قسمت Files روی Add File کلیک و در منوی باز شده روی Upload files کلیک کنید 

8 - روی Drag files/folders here or click to browse from your computer.  کلیک کرده و محتویات پوشه SubNG رو انتخاب کنید  و در پایین صفحه روی Commit changes کلیک کنید . 


حدود 5 الی 10 دقیقه بعد سرور بالا میاد 

و فرایند راه اندازی هم به پایان رسید 
. 
----------
### نحوه استفاده 🟢

برای استفاده از لینک ساب اختصاصی خود در صفحه اصلی space روی سه نقطه بالا در کنار Setting کلیک کرده و بعد روی Embed this space  کلیک کنید .  لینک داده شده رو کپی کنید 

در حالت عادی اگر این لینک رو باز کنید با ارور Invalid key  مواجه میشید برای رفع این ارور باید SessionKey که به فایل SessionMaker.py برای رمزنگاری اطلاعاتتون دادید رو در قالب یک Query params به لینکتون اضافه کنید تا بتونه در صورت صحیح بودن کلید اطلاعات رو رمزگشایی و به تلگرامتون وارد شه . 

نمونه لینک صحیح : 

https://example?key=SessionKey
 

بعد ساخت لینک صحیح به صورت deffult خودش 100 پیام اخر هر کانال/گروه تلگرامی که بهش دادید رو میگرده و کانفیگ ها رو استخراج میکنه اگر خواستید تعداد پیام اخر کم تر باشه لینکتون رو به شکل زیر تغییر بدید 

https://example?key=SessionKey&limit=15

حالا 15 تا پیام اخر رو میگرده دقت کنید عددی که limit میدید باید بین 14 و 201 باشه .

حالا لینکی که ساختید رو میتونیدهم در قسمت subscription ها وارد کنید و هم هر دفعه که نیاز بود خودتون در مرورگرتون بازش کنید تا کانفیگ های تازه و سالم رو مستقیم از تلگرام دریافت کنید.

#

نکات قابل توجه 🔴

1 - برای دریافت کانفیگ های خوب در انتخاب کانال ها گروه های هدف دقت کنید

1 - کلیدتون رو در اختیار کسی قرار ندید

حدود 10 یا 12 تا کانال و یا گروه رو حتما تعریف کنید

4 - از درخواست های پشت سر هم یا اشتراک گذاری لینک sub خودداری کنید

5 - کانفیگ های خروجی رو به در هر client که هستید به صورت دسته جمعی Real delay بگیرید تا کانفیگ های سالم براتون لیست شه . 

6 - اگر به اوپراتور جدید وصل میشید یا کانفیگ ها قطع میشد سعی کنید کانفیگ های جدید رو از لینکتون دریافت و از همشون تست بگیرید

6 - مقدار limit در ساب میتونه تا سقف 200 بشه و 200 تا پیام اخر رو برای استخراج کانفیگ اسکن کنه ولی سعی کنید این عدد رو پایین نگه دارید تا کانفیگ های تازه رو بگیرید به صورت پیشفرض این عدد 100 هست ولی میتونید روی 15 تنظیمش کنید.

#
شاد باشید 😉
