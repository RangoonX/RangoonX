"use client";

import React from "react";
import Link from "next/link";
import Image from "next/image";
import { useLanguage } from "@/context/LanguageContext";
import { ArrowRight, ShieldCheck, Sparkles, Terminal } from "lucide-react";
import { getAssetPath } from "@/utils/paths";

export default function Hero() {
  const { t } = useLanguage();

  return (
    <section className="relative pt-32 pb-20 md:pt-40 md:pb-28 overflow-hidden bg-grid-pattern radial-glow">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          {/* Left Column: Headline & Action */}
          <div className="lg:col-span-7 space-y-6 text-center lg:text-left">
            {/* Main Title */}
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-slate-950 dark:text-white leading-[1.15]">
              {t("hero_title", "Myanmar's Premier Software Engineering Firm")}
            </h1>

            {/* Subtitle */}
            <p className="text-lg sm:text-xl text-slate-800 dark:text-slate-200 leading-relaxed max-w-2xl mx-auto lg:mx-0 font-normal">
              {t("hero_subtitle", "We build robust, high-performance digital solutions designed to scale. From complex cloud architectures to elegant mobile applications.")}
            </p>

            {/* Action Buttons */}
            <div className="pt-2 flex flex-wrap items-center justify-center lg:justify-start gap-4">
              <Link
                href="/services"
                className="inline-flex items-center gap-2.5 px-7 py-3.5 rounded-xl font-bold text-white bg-sky-600 hover:bg-sky-500 shadow-lg shadow-sky-600/30 transition-all duration-200 hover:-translate-y-0.5 cursor-pointer"
              >
                <span>{t("explore_services", "Explore Services")}</span>
                <ArrowRight className="w-4 h-4" />
              </Link>
              <Link
                href="/contact"
                className="inline-flex items-center gap-2 px-7 py-3.5 rounded-xl font-bold text-slate-900 dark:text-white bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 border-2 border-slate-300 dark:border-slate-700 transition-all duration-200 hover:-translate-y-0.5 cursor-pointer shadow-md"
              >
                <span>{t("contact_sales", "Contact Sales")}</span>
              </Link>
            </div>
          </div>

          {/* Right Column: Hero Visual Asset */}
          <div className="lg:col-span-5 relative">
            {/* Ambient Backlight Glow */}
            <div className="absolute -inset-1.5 bg-gradient-to-r from-sky-600 to-[#00d1ff] rounded-2xl blur-xl opacity-40 dark:opacity-50"></div>

            {/* Visual Container */}
            <div className="relative rounded-2xl overflow-hidden border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 shadow-2xl">
              <div className="relative aspect-[4/3] w-full">
                <Image
                  src={getAssetPath("/images/banner.png")}
                  alt="RangoonX Engineering Workspace"
                  fill
                  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 40vw"
                  className="object-cover"
                  priority
                  fetchPriority="high"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
