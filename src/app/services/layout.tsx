import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "နည်းပညာဝန်ဆောင်မှုများ (Services)",
  description:
    "RangoonX ၏ နည်းပညာဝန်ဆောင်မှုများ - Specialized Customized Software၊ Cloud နည်းပညာဝန်ဆောင်မှု၊ AI and Data Analytics၊ IoT and Electronic နှင့် Enterprise POS/ERP စနစ်များ။",
  openGraph: {
    title: "နည်းပညာဝန်ဆောင်မှုများ | RangoonX Software House",
    description:
      "Specialized Customized Software၊ Cloud၊ AI & Data Analytics၊ IoT၊ ERP & POS Solutions တည်ဆောက်ပေးသော Software House။",
    url: "https://rangoonx.github.io/RangoonX/services",
    images: [
      {
        url: "https://rangoonx.github.io/RangoonX/images/og-preview.png",
        secureUrl: "https://rangoonx.github.io/RangoonX/images/og-preview.png",
        width: 1200,
        height: 630,
        type: "image/png",
        alt: "RangoonX Software House - နည်းပညာဝန်ဆောင်မှုများ",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "နည်းပညာဝန်ဆောင်မှုများ | RangoonX Software House",
    description:
      "Specialized Customized Software၊ Cloud၊ AI & Data Analytics၊ IoT၊ ERP & POS Solutions",
    images: ["https://rangoonx.github.io/RangoonX/images/og-preview.png"],
  },
};

export default function ServicesLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
