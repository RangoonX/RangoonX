"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import { Shield, Zap, Cloud, Award } from "lucide-react";

export default function StatsBar() {
  const { t } = useLanguage();

  const stats = [
    {
      icon: Shield,
      title: t("stats_uptime", "Enterprise Grade"),
      desc: t("stats_uptime_desc", "Maximum Reliability"),
    },
    {
      icon: Zap,
      title: t("stats_delivery", "Agile Delivery"),
      desc: t("stats_delivery_desc", "Continuous CI/CD"),
    },
    {
      icon: Cloud,
      title: t("stats_cloud", "Cloud Native"),
      desc: t("stats_cloud_desc", "AWS, GCP & Azure"),
    },
    {
      icon: Award,
      title: t("stats_security", "Bank-Grade"),
      desc: t("stats_security_desc", "Strict Security Standards"),
    },
  ];

  return (
    <section className="relative z-20 -mt-6 sm:-mt-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6 p-6 sm:p-8 rounded-2xl bg-white dark:bg-slate-900 border-2 border-slate-300 dark:border-slate-700 shadow-xl">
        {stats.map((stat, idx) => {
          const Icon = stat.icon;
          return (
            <div key={idx} className="flex flex-col items-center sm:items-start text-center sm:text-left space-y-1.5 p-2">
              <div className="w-11 h-11 rounded-xl bg-sky-100 dark:bg-sky-950 border border-sky-300 dark:border-sky-500/40 flex items-center justify-center text-sky-700 dark:text-sky-300 mb-2 shadow-sm">
                <Icon className="w-6 h-6" />
              </div>
              <h3 className="text-2xl sm:text-3xl font-black tracking-tight text-slate-950 dark:text-white">
                {stat.title}
              </h3>
              <p className="text-xs sm:text-sm text-slate-700 dark:text-slate-300 font-semibold">
                {stat.desc}
              </p>
            </div>
          );
        })}
      </div>
    </section>
  );
}
