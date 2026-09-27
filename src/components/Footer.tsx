"use client";

import React from "react";
import Link from "next/link";
import Image from "next/image";
import { useLanguage } from "@/context/LanguageContext";
import companyInfo from "@/data/company_info.json";
import { 
  Mail, 
  Phone, 
  MapPin, 
  ArrowUpRight, 
  MessageSquare
} from "lucide-react";

export default function Footer() {
  const { t } = useLanguage();

  return (
    <footer className="border-t-2 border-slate-300 dark:border-slate-800 bg-slate-200/90 dark:bg-[#05080e] text-slate-800 dark:text-slate-200 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14 lg:py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 lg:gap-8">
          {/* Brand Info */}
          <div className="lg:col-span-2 space-y-4">
            <Link href="/" className="inline-flex items-center gap-3">
              <Image
                src="/icons/Icon-512.png"
                alt="RangoonX"
                width={32}
                height={32}
                className="w-8 h-8 object-contain"
              />
              <span className="text-xl font-extrabold tracking-tight text-slate-950 dark:text-white">
                {t("brand_name", "RangoonX")}
              </span>
            </Link>
            <p className="text-sm font-medium leading-relaxed max-w-sm text-slate-800 dark:text-slate-200">
              {t("footer_slogan", "Precision Engineering for the Digital Era.")}
            </p>
          </div>

          {/* Navigation Links */}
          <div className="space-y-4">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-950 dark:text-white font-mono">
              Company
            </h3>
            <ul className="space-y-2.5 text-sm font-semibold">
              <li>
                <Link href="/" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("nav_home", "Home")}
                </Link>
              </li>
              <li>
                <Link href="/services" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("nav_services", "Services")}
                </Link>
              </li>
              <li>
                <Link href="/contact" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("nav_contact", "Contact")}
                </Link>
              </li>
            </ul>
          </div>

          {/* Core Solutions */}
          <div className="space-y-4">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-950 dark:text-white font-mono">
              {t("solutions", "Solutions")}
            </h3>
            <ul className="space-y-2.5 text-sm font-semibold">
              <li>
                <Link href="/services" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("custom_software_title", "Custom Software")}
                </Link>
              </li>
              <li>
                <Link href="/services" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("pos_erp_title", "Enterprise POS & ERP Software")}
                </Link>
              </li>
              <li>
                <Link href="/services" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("cloud_title", "Cloud Native Architecture")}
                </Link>
              </li>
              <li>
                <Link href="/services" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("ai_ml_title", "AI & Machine Learning")}
                </Link>
              </li>
              <li>
                <Link href="/services" className="hover:text-sky-600 dark:hover:text-white transition-colors">
                  {t("iot_elec_title", "IoT & Electronic Solutions")}
                </Link>
              </li>
            </ul>
          </div>

          {/* Direct Connect / HQ */}
          <div className="space-y-4">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-950 dark:text-white font-mono">
              {t("connect", "Connect")}
            </h3>
            <ul className="space-y-3 text-sm font-semibold">
              <li>
                <a
                  href={companyInfo.phone_url}
                  className="flex items-center gap-2 hover:text-sky-600 dark:hover:text-white transition-colors"
                >
                  <Phone className="w-4 h-4 text-sky-600 dark:text-sky-400 shrink-0" />
                  <span>{companyInfo.phone}</span>
                </a>
              </li>
              <li>
                <a
                  href={companyInfo.email_url}
                  className="flex items-center gap-2 hover:text-sky-600 dark:hover:text-white transition-colors"
                >
                  <Mail className="w-4 h-4 text-sky-600 dark:text-sky-400 shrink-0" />
                  <span>{companyInfo.email}</span>
                </a>
              </li>
              <li>
                <a
                  href={companyInfo.viber_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 hover:text-sky-600 dark:hover:text-white transition-colors"
                >
                  <MessageSquare className="w-4 h-4 text-purple-600 dark:text-purple-400 shrink-0" />
                  <span>Viber Official</span>
                  <ArrowUpRight className="w-3.5 h-3.5 opacity-80" />
                </a>
              </li>
              <li>
                <a
                  href={companyInfo.maps_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-start gap-2 hover:text-sky-600 dark:hover:text-white transition-colors"
                >
                  <MapPin className="w-4 h-4 text-rose-600 dark:text-rose-400 shrink-0 mt-0.5" />
                  <span className="text-xs leading-snug">{companyInfo.address}</span>
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-12 pt-8 border-t-2 border-slate-300 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-semibold text-slate-700 dark:text-slate-300">
          <p>{t("copyright", "© 2026 RangoonX Software House. Precision Engineering.")}</p>
          <div className="flex items-center gap-6">
            <span className="text-sky-700 dark:text-sky-400 font-mono font-bold">Yangon, Myanmar</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
