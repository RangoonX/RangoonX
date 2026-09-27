import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "နည်းပညာဝန်ဆောင်မှုများ (Services)",
  description:
    "RangoonX ၏ နည်းပညာဝန်ဆောင်မှုများ - Specialized Customized Software၊ Cloud နည်းပညာဝန်ဆောင်မှု၊ AI and Data Analytics၊ IoT and Electronic နှင့် Enterprise POS/ERP စနစ်များ။",
  openGraph: {
    title: "နည်းပညာဝန်ဆောင်မှုများ | RangoonX Software House",
    description:
      "Specialized Customized Software၊ Cloud၊ AI & Data Analytics၊ IoT၊ ERP & POS Solutions တည်ဆောက်ပေးသော Software House။",
    url: "https://rangoonx.com/services",
  },
};

export default function ServicesLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
