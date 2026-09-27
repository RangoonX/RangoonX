"use client";

import React from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { 
  Cloud, 
  Code2, 
  Smartphone, 
  BrainCircuit, 
  ShoppingBag,
  Cpu,
  ArrowRight
} from "lucide-react";

export default function CapabilitiesSection() {
  const { t } = useLanguage();

  const capabilities = [
    {
      icon: Code2,
      titleKey: "custom_software_title",
      descKey: "custom_software_desc",
      tags: ["Enterprise Web", "Python / Node", "Next.js", "Clean Architecture"],
      accent: "text-blue-600 dark:text-blue-400",
      iconBg: "bg-blue-100 dark:bg-blue-950 border-blue-300 dark:border-blue-500/40",
    },
    {
      icon: ShoppingBag,
      titleKey: "pos_erp_title",
      descKey: "pos_erp_desc",
      tags: ["Cloud POS", "Multi-warehouse", "Accounting ERP", "Inventory Sync"],
      accent: "text-amber-600 dark:text-amber-400",
      iconBg: "bg-amber-100 dark:bg-amber-950 border-amber-300 dark:border-amber-500/40",
    },
    {
      icon: Cloud,
      titleKey: "cloud_title",
      descKey: "cloud_desc",
      tags: ["AWS", "Google Cloud", "Docker", "Microservices"],
      accent: "text-sky-600 dark:text-sky-400",
      iconBg: "bg-sky-100 dark:bg-sky-950 border-sky-300 dark:border-sky-500/40",
    },
    {
      icon: BrainCircuit,
      titleKey: "ai_ml_title",
      descKey: "ai_ml_desc",
      tags: ["LLM Agents", "Predictive Analytics", "Process Automation", "RAG"],
      accent: "text-purple-600 dark:text-purple-400",
      iconBg: "bg-purple-100 dark:bg-purple-950 border-purple-300 dark:border-purple-500/40",
    },
    {
      icon: Smartphone,
      titleKey: "mobile_eng_title",
      descKey: "mobile_eng_desc",
      tags: ["Flutter", "iOS & Android", "Offline First", "Native Performance"],
      accent: "text-indigo-600 dark:text-indigo-400",
      iconBg: "bg-indigo-100 dark:bg-indigo-950 border-indigo-300 dark:border-indigo-500/40",
    },
    {
      icon: Cpu,
      titleKey: "iot_elec_title",
      descKey: "iot_elec_desc",
      tags: ["Smart Sensors", "Micro-controllers", "Hardware Telemetry", "Firmware"],
      accent: "text-teal-600 dark:text-teal-400",
      iconBg: "bg-teal-100 dark:bg-teal-950 border-teal-300 dark:border-teal-500/40",
    },
  ];

  return (
    <section className="py-24 relative overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-md bg-sky-100 dark:bg-sky-950 text-sky-900 dark:text-sky-300 border border-sky-300 dark:border-sky-500/40 text-xs font-mono font-bold uppercase shadow-sm">
              Core Expertise
            </div>
            <h2 className="text-3xl sm:text-4xl font-black tracking-tight text-slate-950 dark:text-white">
              {t("our_capabilities", "Our Capabilities")}
            </h2>
            <p className="text-base sm:text-lg text-slate-800 dark:text-slate-200 leading-relaxed font-normal">
              {t("capabilities_subtitle", "Engineered for reliability. We leverage modern stacks to deliver uncompromising performance.")}
            </p>
          </div>

          <Link
            href="/services"
            className="inline-flex items-center gap-2 text-sm font-bold text-sky-600 dark:text-sky-400 hover:text-sky-500 transition-colors group self-start md:self-end"
          >
            <span>View All Engineering Services</span>
            <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
          </Link>
        </div>

        {/* Capabilities Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
          {capabilities.map((item, idx) => {
            const Icon = item.icon;
            return (
              <div
                key={idx}
                className="group relative p-8 rounded-2xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 hover:border-sky-500 dark:hover:border-sky-500 transition-all duration-300 shadow-md hover:shadow-xl hover:-translate-y-1 flex flex-col justify-between"
              >
                <div>
                  {/* Icon Header */}
                  <div className={`w-12 h-12 rounded-xl border flex items-center justify-center mb-6 shadow-sm ${item.iconBg}`}>
                    <Icon className={`w-6 h-6 ${item.accent}`} />
                  </div>

                  {/* Title */}
                  <h3 className="text-xl font-bold tracking-tight text-slate-950 dark:text-white mb-3">
                    {t(item.titleKey)}
                  </h3>

                  {/* Description */}
                  <p className="text-sm sm:text-base text-slate-800 dark:text-slate-200 leading-relaxed mb-6 font-normal">
                    {t(item.descKey)}
                  </p>
                </div>

                {/* Tech Tags */}
                <div className="pt-4 border-t border-slate-200 dark:border-slate-800 flex flex-wrap gap-2">
                  {item.tags.map((tag, tagIdx) => (
                    <span
                      key={tagIdx}
                      className="px-3 py-1 text-xs font-bold rounded-md bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-slate-100 border border-slate-300 dark:border-slate-600 font-mono shadow-xs"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
