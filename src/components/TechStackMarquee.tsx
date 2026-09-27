"use client";

import React from "react";
import { 
  Code2, 
  Smartphone, 
  Server, 
  Cloud, 
  Database, 
  Cpu, 
  Layers, 
  GitBranch 
} from "lucide-react";

export default function TechStackMarquee() {
  const technologies = [
    { name: "Next.js / React", icon: Code2, role: "Web Frontend" },
    { name: "Flutter", icon: Smartphone, role: "Cross-Platform Mobile" },
    { name: "Python / FastAPI", icon: Server, role: "Scalable Backend" },
    { name: "AWS & GCP", icon: Cloud, role: "Cloud Infrastructure" },
    { name: "PostgreSQL & Redis", icon: Database, role: "Data Layer" },
    { name: "AI / LLM Orchestration", icon: Cpu, role: "Intelligence" },
    { name: "Docker & Kubernetes", icon: Layers, role: "Containerization" },
    { name: "CI / CD Pipelines", icon: GitBranch, role: "Automated Release" },
  ];

  return (
    <section className="py-14 border-y border-slate-300 dark:border-slate-800 bg-slate-100 dark:bg-slate-950/60">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-8">
          <p className="text-xs uppercase tracking-widest text-slate-800 dark:text-slate-200 font-mono font-bold">
            Engineered With Modern Industrial Stacks
          </p>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3 sm:gap-4">
          {technologies.map((tech, idx) => {
            const Icon = tech.icon;
            return (
              <div
                key={idx}
                className="flex flex-col items-center justify-center p-3.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 hover:border-sky-500 transition-all duration-200 group text-center shadow-sm"
              >
                <Icon className="w-5 h-5 text-sky-600 dark:text-sky-400 mb-2 group-hover:scale-110 transition-transform" />
                <span className="text-xs font-bold text-slate-950 dark:text-white">
                  {tech.name}
                </span>
                <span className="text-[11px] text-slate-600 dark:text-slate-300 mt-0.5 font-medium">
                  {tech.role}
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
