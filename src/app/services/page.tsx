"use client";

import React from "react";
import Image from "next/image";
import { useLanguage } from "@/context/LanguageContext";
import { 
  Code2, 
  Cloud, 
  BrainCircuit, 
  Cpu, 
  ShoppingBag, 
  ShieldCheck, 
  Sparkles,
  CheckCircle2
} from "lucide-react";
import CtaBanner from "@/components/CtaBanner";
import { getAssetPath } from "@/utils/paths";

export default function ServicesPage() {
  const { t } = useLanguage();

  const services = [
    {
      icon: Code2,
      titleKey: "service_1_title",
      descKey: "service_1_desc",
      tags: ["React", "Flutter", "Python", "Node.js"],
      features: [
        "Full-cycle SDLC & Clean Architecture",
        "High-performance REST & GraphQL APIs",
        "Automated Test Coverage (Unit & E2E)",
      ],
      accent: "text-sky-600 dark:text-sky-400",
      iconBg: "bg-sky-100 dark:bg-sky-950 border-sky-300 dark:border-sky-500/40",
    },
    {
      icon: Cloud,
      titleKey: "service_2_title",
      descKey: "service_2_desc",
      tags: ["AWS", "Azure", "Docker", "CI/CD"],
      features: [
        "Zero-downtime Cloud Migrations",
        "Kubernetes & Docker Orchestration",
        "Cost-optimized Serverless Infrastructure",
      ],
      accent: "text-blue-600 dark:text-blue-400",
      iconBg: "bg-blue-100 dark:bg-blue-950 border-blue-300 dark:border-blue-500/40",
    },
    {
      icon: BrainCircuit,
      titleKey: "service_3_title",
      descKey: "service_3_desc",
      tags: ["Machine Learning", "LLM", "Computer Vision"],
      features: [
        "Custom LLM Fine-tuning & RAG Pipelines",
        "Predictive Business Intelligence Models",
        "Computer Vision & OCR Automation",
      ],
      accent: "text-indigo-600 dark:text-indigo-400",
      iconBg: "bg-indigo-100 dark:bg-indigo-950 border-indigo-300 dark:border-indigo-500/40",
    },
    {
      icon: Cpu,
      titleKey: "service_4_title",
      descKey: "service_4_desc",
      tags: ["Embedded", "Sensors", "PCB", "Firmware"],
      features: [
        "IoT Telemetry & Industrial Sensors",
        "Custom Firmware & Micro-controller code",
        "Real-time Hardware Monitoring Dashboards",
      ],
      accent: "text-teal-600 dark:text-teal-400",
      iconBg: "bg-teal-100 dark:bg-teal-950 border-teal-300 dark:border-teal-500/40",
    },
    {
      icon: ShoppingBag,
      titleKey: "service_5_title",
      descKey: "service_5_desc",
      tags: ["ERP Software", "Cloud POS", "Multi-warehouse", "Finance & Inventory"],
      features: [
        "Centralized Multi-outlet Inventory",
        "Cloud-synced POS with Offline Backup",
        "Automated Financial & Sales Analytics",
      ],
      accent: "text-amber-600 dark:text-amber-400",
      iconBg: "bg-amber-100 dark:bg-amber-950 border-amber-300 dark:border-amber-500/40",
    },
    {
      icon: ShieldCheck,
      titleKey: "service_6_title",
      descKey: "service_6_desc",
      tags: ["Maintenance", "Security Audit", "24/7 Monitoring"],
      features: [
        "Continuous Performance Optimization",
        "Penetration Testing & Vulnerability Audits",
        "Proactive 24/7 Server Health Monitoring",
      ],
      accent: "text-emerald-600 dark:text-emerald-400",
      iconBg: "bg-emerald-100 dark:bg-emerald-950 border-emerald-300 dark:border-emerald-500/40",
    },
  ];

  return (
    <div className="pt-28 pb-20">
      {/* Services Header */}
      <section className="py-16 bg-grid-pattern radial-glow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center max-w-4xl space-y-4">
          <h1 className="text-4xl sm:text-5xl font-black tracking-tight text-slate-950 dark:text-white">
            {t("services_page_title", "Our Services")}
          </h1>

          <p className="text-lg text-slate-800 dark:text-slate-200 leading-relaxed max-w-2xl mx-auto font-normal">
            {t("services_page_subtitle", "We deliver precision-engineered software solutions designed to scale. Our expertise spans custom application development, seamless cloud integrations, and advanced AI implementations.")}
          </p>
        </div>
      </section>

      {/* Services 6-Grid */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {services.map((service, idx) => {
              const Icon = service.icon;
              return (
                <div
                  key={idx}
                  className="rounded-2xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 p-8 flex flex-col justify-between hover:border-sky-500 dark:hover:border-sky-500 hover:shadow-2xl transition-all duration-300 group shadow-md"
                >
                  <div>
                    {/* Icon */}
                    <div className={`w-12 h-12 rounded-xl border flex items-center justify-center mb-6 shadow-sm ${service.iconBg}`}>
                      <Icon className={`w-6 h-6 ${service.accent}`} />
                    </div>

                    {/* Title */}
                    <h2 className="text-xl font-bold tracking-tight text-slate-950 dark:text-white mb-3">
                      {t(service.titleKey)}
                    </h2>

                    {/* Description */}
                    <p className="text-sm sm:text-base text-slate-800 dark:text-slate-200 leading-relaxed mb-6 font-normal">
                      {t(service.descKey)}
                    </p>

                    {/* Bullet features */}
                    <ul className="space-y-2.5 mb-6 border-t border-slate-200 dark:border-slate-800 pt-4">
                      {service.features.map((feat, fIdx) => (
                        <li key={fIdx} className="flex items-center gap-2 text-xs text-slate-900 dark:text-slate-100 font-semibold">
                          <CheckCircle2 className="w-4 h-4 text-sky-600 dark:text-sky-400 shrink-0" />
                          <span>{feat}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* Tags */}
                  <div className="pt-4 border-t border-slate-200 dark:border-slate-800 flex flex-wrap gap-2">
                    {service.tags.map((tag, tIdx) => (
                      <span
                        key={tIdx}
                        className="px-2.5 py-1 text-xs font-mono font-bold rounded-md bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-slate-100 border border-slate-300 dark:border-slate-600 shadow-xs"
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

      {/* Feature Showcase Banner Asset */}
      <section className="py-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="relative rounded-3xl overflow-hidden border-2 border-slate-300 dark:border-slate-700 shadow-2xl">
          <div className="relative aspect-[21/9] min-h-[300px] w-full">
            <Image
              src={getAssetPath("/images/service_banner.png")}
              alt="RangoonX Services Overview"
              fill
              sizes="(max-width: 1280px) 100vw, 1280px"
              className="object-cover"
              loading="lazy"
            />
            {/* Gradient Overlay */}
            <div className="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/60 to-transparent flex flex-col justify-end p-8 sm:p-12">
              <div className="max-w-2xl space-y-3">
                <span className="text-xs font-mono font-bold uppercase text-sky-400 tracking-wider">
                  Enterprise Quality
                </span>
                <h3 className="text-2xl sm:text-3xl font-black text-white">
                  Engineered to withstand enterprise-scale concurrency
                </h3>
                <p className="text-sm sm:text-base text-slate-200 font-medium">
                  Our systems are tested under high load and optimized for Myanmar and global network realities.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Call to action */}
      <CtaBanner />
    </div>
  );
}
