"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import { Layers, Gauge, Handshake } from "lucide-react";

export default function WhyUs() {
  const { t } = useLanguage();

  const pillars = [
    {
      icon: Layers,
      title: t("why_pillar_1_title", "Architecture First"),
      desc: t("why_pillar_1_desc", "We build clean, modular architectures that prevent technical debt and allow your systems to scale effortlessly."),
    },
    {
      icon: Gauge,
      title: t("why_pillar_2_title", "Speed & Performance"),
      desc: t("why_pillar_2_desc", "Sub-second load times, optimized databases, and responsive interfaces engineered for real-world network conditions."),
    },
    {
      icon: Handshake,
      title: t("why_pillar_3_title", "Continuous Partnership"),
      desc: t("why_pillar_3_desc", "Beyond initial launch, we provide ongoing architectural support, monitoring, and proactive feature enhancements."),
    },
  ];

  return (
    <section className="py-24 bg-slate-100/70 dark:bg-slate-950/80 border-t-2 border-slate-200 dark:border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto mb-16 space-y-4">
          <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-md bg-sky-100 dark:bg-sky-950 text-sky-900 dark:text-sky-300 border border-sky-300 dark:border-sky-500/40 text-xs font-mono font-bold uppercase shadow-sm">
            Engineering Principles
          </div>
          <h2 className="text-3xl sm:text-4xl font-black tracking-tight text-slate-950 dark:text-white">
            {t("why_us_title", "Why RangoonX?")}
          </h2>
          <p className="text-base sm:text-lg text-slate-800 dark:text-slate-200 leading-relaxed font-normal">
            {t("why_us_subtitle", "We bring every project to life with great design, scalable systems, and affordable pricing.")}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {pillars.map((pillar, idx) => {
            const Icon = pillar.icon;
            return (
              <div
                key={idx}
                className="p-8 rounded-2xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 shadow-md relative"
              >
                <div className="w-12 h-12 rounded-xl bg-sky-100 dark:bg-sky-950 border border-sky-300 dark:border-sky-500/40 flex items-center justify-center text-sky-700 dark:text-sky-300 mb-6 shadow-sm">
                  <Icon className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold tracking-tight text-slate-950 dark:text-white mb-3">
                  {pillar.title}
                </h3>
                <p className="text-sm sm:text-base text-slate-800 dark:text-slate-200 leading-relaxed font-normal">
                  {pillar.desc}
                </p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
