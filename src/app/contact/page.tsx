"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import ContactForm from "@/components/ContactForm";
import { Sparkles } from "lucide-react";

export default function ContactPage() {
  const { t } = useLanguage();

  return (
    <div className="pt-28 pb-24">
      {/* Header */}
      <section className="py-16 bg-grid-pattern radial-glow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center max-w-3xl space-y-4">
          <h1 className="text-4xl sm:text-5xl font-black tracking-tight text-slate-950 dark:text-white">
            {t("contact_page_title", "Let's build together.")}
          </h1>

          <p className="text-lg text-slate-800 dark:text-slate-200 leading-relaxed font-normal">
            {t("contact_page_subtitle", "Reach out to discuss custom software solutions, cloud migrations, or how we can integrate AI into your workflow.")}
          </p>
        </div>
      </section>

      {/* Main Content: Form + Office Details */}
      <section className="py-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <ContactForm />
      </section>
    </div>
  );
}
