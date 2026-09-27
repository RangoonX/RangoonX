import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "ဆက်သွယ်ရန် (Contact Us)",
  description:
    "RangoonX Software House သို့ ဆက်သွယ်ရန် - HAGL Myanmar Centre ရုံးခန်း၊ ဖုန်း (+959 785955940)၊ အီးမေးလ် သို့မဟုတ် ပရောဂျက် မေးမြန်းမှုများ အခမဲ့ ဆွေးနွေးတိုင်ပင်နိုင်ပါသည်။",
  openGraph: {
    title: "ဆက်သွယ်ရန် | RangoonX Software House",
    description:
      "သင်၏ နည်းပညာလိုအပ်ချက်များနှင့် ပရောဂျက်များကို RangoonX အင်ဂျင်နီယာအဖွဲ့နှင့် ဆွေးနွေးတိုင်ပင်ရန် ဆက်သွယ်ပါ။",
    url: "https://rangoonx.com/contact",
  },
};

export default function ContactLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
