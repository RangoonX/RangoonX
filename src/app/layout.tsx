import type { Metadata, Viewport } from "next";
import "./globals.css";
import { padauk, inter } from "./fonts";
import { LanguageProvider } from "@/context/LanguageContext";
import { ThemeProvider } from "@/context/ThemeContext";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const siteUrl = "https://rangoonx.com";

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#070b12" },
  ],
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "RangoonX | သင့်လုပ်ငန်းအတွက် နည်းပညာဝန်ဆောင်မှု - Software House",
    template: "%s | RangoonX Software House",
  },
  description:
    "RangoonX သည် မြန်မာနိုင်ငံရှိ စီးပွားရေးလုပ်ငန်းများအတွက် Specialized Customized Software၊ Cloud နည်းပညာဝန်ဆောင်မှု၊ AI and Data Analytics၊ IoT and Electronic နှင့် Enterprise POS/ERP စနစ်များကို အဆင့်မြင့် တည်ဆောက်ပေးသော Software House ဖြစ်ပါသည်။",
  keywords: [
    "RangoonX",
    "RangoonX Software House",
    "Software House Myanmar",
    "Software Development Yangon",
    "ERP Software Myanmar",
    "POS Software Myanmar",
    "Enterprise POS ERP Systems",
    "Point of Sale System Myanmar",
    "Cloud POS System Yangon",
    "Warehouse Inventory ERP",
    "Accounting Software Myanmar",
    "အရောင်းဆိုင်သုံး POS စနစ်",
    "ကုန်ပစ္စည်း စာရင်းကိုင် ERP Software",
    "Specialized Customized Software",
    "သင့်လုပ်ငန်းအတွက် နည်းပညာဝန်ဆောင်မှု",
    "သင့်လုပ်ငန်းအတွက် RangoonX နည်းပညာ",
    "Web Development Myanmar",
    "Mobile App Development Yangon",
    "Cloud Migration AWS Azure",
    "AI and Data Analytics Myanmar",
    "IoT and Electronic Myanmar",
    "မြန်မာ Software ကုမ္ပဏီ",
    "ဆော့ဖ်ဝဲ ရေးဆွဲခြင်း ရန်ကုန်",
  ],
  authors: [{ name: "RangoonX", url: siteUrl }],
  creator: "RangoonX Software House",
  publisher: "RangoonX Software House",
  alternates: {
    canonical: "/",
    languages: {
      "my-MM": "/",
      "en-US": "/",
    },
  },
  openGraph: {
    type: "website",
    locale: "my_MM",
    alternateLocale: ["en_US"],
    url: siteUrl,
    siteName: "RangoonX Software House",
    title: "RangoonX | သင့်လုပ်ငန်းအတွက် နည်းပညာဝန်ဆောင်မှု",
    description:
      "Specialized Customized Software၊ Cloud နည်းပညာဝန်ဆောင်မှု၊ AI and Data Analytics၊ IoT and Electronic နှင့် Enterprise POS/ERP စနစ်များ တည်ဆောက်ပေးသော Software House။",
    images: [
      {
        url: "/images/banner.png",
        width: 1200,
        height: 630,
        alt: "RangoonX Software House - သင့်လုပ်ငန်းအတွက် နည်းပညာဝန်ဆောင်မှု",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "RangoonX | Software House Myanmar",
    description:
      "သင့်လုပ်ငန်းအတွက် နည်းပညာဝန်ဆောင်မှု - Specialized Customized Software, Cloud, AI & Data Analytics, IoT.",
    images: ["/images/banner.png"],
    creator: "@rangoonx_official",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  icons: {
    icon: [
      { url: "/favicon.png", sizes: "32x32", type: "image/png" },
      { url: "/icons/Icon-512.png", sizes: "512x512", type: "image/png" },
    ],
    apple: [
      { url: "/apple-touch-icon.png", sizes: "180x180", type: "image/png" },
    ],
  },
};

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  name: "RangoonX Software House",
  alternateName: "RangoonX",
  url: siteUrl,
  logo: `${siteUrl}/icons/Icon-512.png`,
  image: `${siteUrl}/images/banner.png`,
  description:
    "သင့်လုပ်ငန်းအတွက် နည်းပညာဝန်ဆောင်မှု - Specialized Customized Software, Cloud Architecture, AI and Data Analytics, IoT and Electronic, Enterprise POS & ERP Systems.",
  telephone: "+959785955940",
  email: "rangoonx.com@gmail.com",
  address: {
    "@type": "PostalAddress",
    streetAddress: "Level 8, Tower B, HAGL Myanmar Centre",
    addressLocality: "Yangon",
    addressRegion: "Yangon Region",
    addressCountry: "MM",
  },
  sameAs: [
    "https://www.tiktok.com/@rangoonx_official",
    "https://maps.google.com/?q=HAGL+Myanmar+Centre",
  ],
  priceRange: "$$",
  areaServed: {
    "@type": "Country",
    name: "Myanmar",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="mm"
      className={`${inter.variable} ${padauk.variable} h-full antialiased`}
      suppressHydrationWarning
    >
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="min-h-full flex flex-col bg-white dark:bg-[#070b12] text-slate-950 dark:text-slate-100 transition-colors duration-200">
        <ThemeProvider>
          <LanguageProvider>
            <div className="flex flex-col min-h-screen">
              <Navbar />
              <main className="flex-1">{children}</main>
              <Footer />
            </div>
          </LanguageProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
