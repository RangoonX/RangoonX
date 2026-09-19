# src/config/localization.py

import json
import os
from config import logger

DEFAULT_EN = {
    "app_title": "Rangoon X | Software House",
    "brand_name": "RangoonX",
    "nav_home": "Home",
    "nav_services": "Services",
    "nav_projects": "Projects",
    "nav_contact": "Contact",
    "hero_tag": "PRECISION ENGINEERING",
    "hero_title": "End-to-End Technology Solutions for Modern Business",
    "hero_subtitle": "From IoT hardware integration and AI automation to enterprise ERP and POS systems — we engineer complete digital ecosystems that scale with your business.",
    "explore_services": "Explore Services",
    "contact_sales": "Contact Sales",
    "our_capabilities": "Our Capabilities",
    "capabilities_subtitle": "Full-stack engineering across software, hardware, and intelligent automation.",
    "cloud_title": "Cloud & DevOps",
    "cloud_desc": "Scalable cloud infrastructure on AWS and Google Cloud with CI/CD pipelines, containerization, and microservices architecture.",
    "custom_software_title": "ERP & POS Systems",
    "custom_software_desc": "Custom enterprise resource planning and point-of-sale solutions tailored to streamline operations, inventory, and business workflows.",
    "mobile_eng_title": "IoT & Electronics",
    "mobile_eng_desc": "End-to-end IoT solutions — from embedded firmware and sensor integration to real-time dashboards and hardware prototyping.",
    "ai_ml_title": "AI & Automation",
    "ai_ml_desc": "Intelligent automation powered by machine learning, computer vision, and generative AI to transform business processes.",
    "footer_slogan": "Precision Engineering for the Digital Era.",
    "solutions": "Solutions",
    "connect": "Connect",
    "copyright": "© 2026 RangoonX Software House. Precision Engineering.",
    "services_page_title": "Our Services",
    "services_page_subtitle": "We deliver end-to-end technology solutions — from custom software and cloud infrastructure to IoT hardware, AI automation, ERP, and POS systems.",
    "service_1_title": "Custom Software & Mobile Apps",
    "service_1_desc": "Bespoke web and mobile applications built with modern frameworks. From enterprise portals to consumer apps — engineered for performance, security, and scale.",
    "service_2_title": "Cloud & DevOps Infrastructure",
    "service_2_desc": "Design and migrate to scalable cloud environments on AWS and Azure. Automated CI/CD pipelines, containerized microservices, and infrastructure as code.",
    "service_3_title": "AI, ML & Intelligent Automation",
    "service_3_desc": "Deploy machine learning models, computer vision systems, and LLM-powered workflows. From predictive analytics to fully automated business processes.",
    "service_4_title": "IoT, Electronics & Hardware",
    "service_4_desc": "Complete IoT solutions — embedded systems, sensor networks, PCB design, firmware development, and real-time monitoring dashboards for industrial and commercial use.",
    "service_5_title": "ERP & POS Systems",
    "service_5_desc": "Tailored enterprise resource planning and point-of-sale platforms. Inventory management, financial reporting, multi-branch operations, and seamless integrations.",
    "service_6_title": "Enterprise Support & Security",
    "service_6_desc": "24/7 system monitoring, security audits, performance optimization, and dedicated SLA-backed support for your mission-critical infrastructure.",
    "services_cta_title": "Ready to start a project?",
    "services_cta_desc": "Contact our engineering team to discuss your requirements — software, hardware, or both.",
    "get_in_touch": "Get in Touch",
    "contact_page_title": "Let's build together.",
    "contact_page_subtitle": "Reach out to discuss custom software, IoT solutions, AI integration, ERP/POS systems, or any technology need.",
    "contact_hq_title": "HQ",
    "contact_hq_address": "Level 8, Tower B, HAGL Myanmar Centre, Yangon, Myanmar",
    "contact_email_title": "Email",
    "contact_phone_title": "Phone",
    "form_first_name": "First Name",
    "form_last_name": "Last Name",
    "form_email": "Work Email",
    "form_interest": "Area of Interest",
    "form_interest_opt1": "Custom Software & Mobile Apps",
    "form_interest_opt2": "Cloud & DevOps Infrastructure",
    "form_interest_opt3": "AI & Intelligent Automation",
    "form_interest_opt4": "IoT, Electronics & Hardware",
    "form_interest_opt5": "ERP & POS Systems",
    "form_interest_opt6": "Other Inquiry",
    "form_message": "Project Details",
    "form_submit": "Send Inquiry",
    "form_success": "Thank you for reaching out! We will contact you shortly.",
}

DEFAULT_MM = {
    "app_title": "ရန်ကုန် X | ဆော့ဖ်ဝဲလ် အိမ်တော်",
    "brand_name": "RangoonX",
    "nav_home": "ပင်မစာမျက်နှာ",
    "nav_services": "ဝန်ဆောင်မှုများ",
    "nav_projects": "စီမံကိန်းများ",
    "nav_contact": "ဆက်သွယ်ရန်",
    "hero_tag": "သင့်လုပ်ငန်းအတွက် System",
    "hero_title": "စီးပွားရေးလုပ်ငန်းများအတွက် အကောင်းဆုံးရွေးချယ်မှု",
    "hero_subtitle": "IoT စနစ်များ၊ AI အလိုအလျောက်စနစ်များ၊ ERP နှင့် POS စနစ်များမှသည် Cloud နှင့် ဆော့ဖ်ဝဲလ် ရေးဆွဲခြင်းအထိ — သင့်လုပ်ငန်းနှင့်အတူ ကြီးထွားနိုင်သော ဒီဂျစ်တယ် စနစ်များကို တည်ဆောက်ပေးပါသည်။",
    "explore_services": "ဝန်ဆောင်မှုများ ကြည့်ရှုရန်",
    "contact_sales": "ဆက်သွယ်မေးမြန်းရန်",
    "our_capabilities": "ကျွမ်းကျင်မှုနှင့် ဝန်ဆောင်မှုများ",
    "capabilities_subtitle": "ဆော့ဖ်ဝဲလ်၊ ဟာ့ဒ်ဝဲနှင့် AI အလိုအလျောက်စနစ်များ — အစအဆုံး နည်းပညာ ဝန်ဆောင်မှုများ။",
    "cloud_title": "Cloud & DevOps",
    "cloud_desc": "AWS နှင့် Google Cloud ပေါ်တွင် CI/CD pipeline များ၊ container စနစ်များနှင့် microservices ဗိသုကာဖြင့် တည်ဆောက်ထားသော cloud အခြေခံအဆောက်အအုံများ။",
    "custom_software_title": "ERP & POS စနစ်များ",
    "custom_software_desc": "လုပ်ငန်းလည်ပတ်မှု၊ ကုန်ပစ္စည်းစီမံခန့်ခွဲမှုနှင့် လုပ်ငန်းစဉ်များကို ချောမွေ့စေမည့် စိတ်ကြိုက် ERP နှင့် POS ဆော့ဖ်ဝဲလ်များ။",
    "mobile_eng_title": "IoT & အီလက်ထရောနစ်",
    "mobile_eng_desc": "Embedded firmware၊ sensor ပေါင်းစပ်ခြင်းမှ real-time dashboard များအထိ — IoT ဖြေရှင်းချက်များနှင့် ဟာ့ဒ်ဝဲ ဒီဇိုင်းများ။",
    "ai_ml_title": "AI & အလိုအလျောက်စနစ်",
    "ai_ml_desc": "Machine Learning၊ Computer Vision နှင့် Generative AI ဖြင့် လုပ်ငန်းစဉ်များကို ပြောင်းလဲပေးမည့် ဉာဏ်ရည်တု အလိုအလျောက်စနစ်များ။",
    "footer_slogan": "ဒီဂျစ်တယ်ခေတ်အတွက် တိကျသေချာသော နည်းပညာ အင်ဂျင်နီယာ။",
    "solutions": "ဝန်ဆောင်မှုများ",
    "connect": "ဆက်သွယ်ရန်",
    "copyright": "© ၂၀၂၆ RangoonX Software House။ မူပိုင်ခွင့်များ သိမ်းဆည်းထားပြီးဖြစ်သည်။",
    "services_page_title": "ကျွန်ုပ်တို့၏ ဝန်ဆောင်မှုများ",
    "services_page_subtitle": "ဆော့ဖ်ဝဲလ်နှင့် Cloud စနစ်များမှသည် IoT ဟာ့ဒ်ဝဲ၊ AI အလိုအလျောက်စနစ်၊ ERP နှင့် POS စနစ်များအထိ — အစအဆုံး နည်းပညာဝန်ဆောင်မှုများ ပေးပါသည်။",
    "service_1_title": "စိတ်ကြိုက် ဆော့ဖ်ဝဲလ် & Mobile App များ",
    "service_1_desc": "ခေတ်မီ framework များဖြင့် တည်ဆောက်ထားသော လုပ်ငန်းသုံး web နှင့် mobile application များ — စွမ်းဆောင်ရည်၊ လုံခြုံမှုနှင့် တိုးချဲ့နိုင်မှုကို အဓိကထားပါသည်။",
    "service_2_title": "Cloud & DevOps အခြေခံအဆောက်အအုံ",
    "service_2_desc": "AWS နှင့် Azure Cloud ပေါ်တွင် အလိုအလျောက် CI/CD pipeline များ၊ container microservices နှင့် Infrastructure as Code ဖြင့် တည်ဆောက်ခြင်း။",
    "service_3_title": "AI, ML & အလိုအလျောက်စနစ်",
    "service_3_desc": "Machine Learning model များ၊ Computer Vision စနစ်များနှင့် LLM-powered workflow များ — ကြိုတင်ခန့်မှန်းခြင်းမှ လုပ်ငန်းစဉ် အလိုအလျောက်စနစ်အထိ။",
    "service_4_title": "IoT, အီလက်ထရောနစ် & ဟာ့ဒ်ဝဲ",
    "service_4_desc": "Embedded system များ၊ sensor network များ၊ PCB ဒီဇိုင်း၊ firmware ရေးဆွဲခြင်းနှင့် real-time monitoring dashboard များ — စက်မှုလုပ်ငန်းနှင့် စီးပွားရေးသုံး IoT ဖြေရှင်းချက်များ။",
    "service_5_title": "ERP & POS စနစ်များ",
    "service_5_desc": "ကုန်ပစ္စည်းစီမံခန့်ခွဲမှု၊ ငွေကြေးအစီရင်ခံခြင်း၊ ဘဏ်ခွဲစနစ်များနှင့် ပေါင်းစပ်မှုများ ပါဝင်သော စိတ်ကြိုက် ERP နှင့် POS platform များ။",
    "service_6_title": "လုပ်ငန်းသုံး စနစ်ထိန်းသိမ်းမှု & လုံခြုံရေး",
    "service_6_desc": "၂၄ နာရီ စနစ်စောင့်ကြည့်ခြင်း၊ လုံခြုံရေးစစ်ဆေးခြင်း၊ စွမ်းဆောင်ရည်ပိုမိုကောင်းမွန်အောင်ပြုလုပ်ခြင်းနှင့် SLA အာမခံချက်ဖြင့် ပံ့ပိုးမှု။",
    "services_cta_title": "ပရောဂျက်တစ်ခု စတင်ရန် အဆင်သင့်ဖြစ်ပြီလား။",
    "services_cta_desc": "ဆော့ဖ်ဝဲလ်၊ ဟာ့ဒ်ဝဲ သို့မဟုတ် နှစ်ခုလုံးအတွက် — ကျွန်ုပ်တို့၏ အင်ဂျင်နီယာ အဖွဲ့ထံ ဆက်သွယ်ပါ။",
    "get_in_touch": "ဆက်သွယ်ရန်",
    "contact_page_title": "အတူတကွ တည်ဆောက်ကြစို့။",
    "contact_page_subtitle": "ဆော့ဖ်ဝဲလ်၊ IoT ဖြေရှင်းချက်များ၊ AI ပေါင်းစပ်မှု၊ ERP/POS စနစ်များ သို့မဟုတ် မည်သည့် နည်းပညာ လိုအပ်ချက်မဆို ဆွေးနွေးရန် ဆက်သွယ်ပါ။",
    "contact_hq_title": "ရုံးချုပ်",
    "contact_hq_address": "အဆောက်အအုံ B၊ အဆင့် ၈၊ HAGL မြန်မာ စင်တာ၊ ရန်ကုန်မြို့။",
    "contact_email_title": "အီးမေးလ်",
    "contact_phone_title": "ဖုန်း",
    "form_first_name": "အမည် (ပထမ)",
    "form_last_name": "အမည် (ဒုတိယ)",
    "form_email": "လုပ်ငန်း အီးမေးလ်",
    "form_interest": "စိတ်ပါဝင်စားသည့် ဝန်ဆောင်မှု",
    "form_interest_opt1": "စိတ်ကြိုက် ဆော့ဖ်ဝဲလ် ရေးဆွဲခြင်း",
    "form_interest_opt2": "Cloud စနစ် တည်ဆောက်ခြင်းနှင့် ရွှေ့ပြောင်းခြင်း",
    "form_interest_opt3": "AI နှင့် Machine Learning ပေါင်းစပ်ခြင်း",
    "form_interest_opt4": "IoT, အီလက်ထရောနစ် & ဟာ့ဒ်ဝဲ",
    "form_interest_opt5": "ERP & POS စနစ်များ",
    "form_interest_opt6": "အခြား မေးမြန်းချက်များ",
    "form_message": "ပရောဂျက် အသေးစိတ်",
    "form_submit": "မေးမြန်းချက် ပေးပို့မည်",
    "form_success": "ကျေးဇူးတင်ရှိပါသည်။ ကျွန်ုပ်တို့၏ အဖွဲ့မှ သင့်ထံ မကြာမီ ဆက်သွယ်ပါမည်။",
}

EMBEDDED_TRANSLATIONS = {
    "en": DEFAULT_EN,
    "mm": DEFAULT_MM,
}


import json
import urllib.request
from config import logger

# ... (DEFAULT_EN, DEFAULT_MM, EMBEDDED_TRANSLATIONS defined above)

class LocalizationManager:
    _translations = {}

    @classmethod
    def load_translations(cls, lang_code: str):
        if lang_code in cls._translations and cls._translations[lang_code]:
            return cls._translations[lang_code]

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        candidate_paths = [
            os.path.join(base_dir, "assets", "lang", f"{lang_code}.json"),
            os.path.join(base_dir, "assets", "langs", f"{lang_code}.json"),
            f"assets/lang/{lang_code}.json",
            f"assets/langs/{lang_code}.json",
            f"lang/{lang_code}.json",
            f"langs/{lang_code}.json",
        ]

        for path in candidate_paths:
            if not os.path.isfile(path):
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    cls._translations[lang_code] = json.load(f)
                    logger.info(f"Loaded JSON translation from: {path}")
                    return cls._translations[lang_code]
            except Exception:
                pass

        for path in candidate_paths:
            try:
                response = urllib.request.urlopen(path)
                data = json.loads(response.read().decode("utf-8"))
                cls._translations[lang_code] = data
                logger.info(f"Loaded JSON translation via HTTP from: {path}")
                return cls._translations[lang_code]
            except Exception:
                pass

        fallback_data = EMBEDDED_TRANSLATIONS.get(lang_code, EMBEDDED_TRANSLATIONS.get("en", {}))
        cls._translations[lang_code] = fallback_data
        return fallback_data

    @classmethod
    def get_string(cls, lang_code: str, key: str) -> str:
        translations = cls.load_translations(lang_code)
        return translations.get(key, key)