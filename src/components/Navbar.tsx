"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";
import { useLanguage } from "@/context/LanguageContext";
import { useTheme } from "@/context/ThemeContext";
import { 
  Menu, 
  X, 
  Sun, 
  Moon, 
  Globe, 
  ArrowRight
} from "lucide-react";

import { getAssetPath } from "@/utils/paths";

export default function Navbar() {
  const { language, toggleLanguage, t } = useLanguage();
  const { theme, toggleTheme } = useTheme();
  const pathname = usePathname();
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const navLinks = [
    { href: "/", labelKey: "nav_home" },
    { href: "/services", labelKey: "nav_services" },
    { href: "/contact", labelKey: "nav_contact" },
  ];

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-200 ${
        isScrolled
          ? "bg-white/95 dark:bg-[#070b12]/95 backdrop-blur-md border-b-2 border-slate-200 dark:border-slate-800 shadow-md"
          : "bg-white/80 dark:bg-[#070b12]/80 backdrop-blur-sm border-b border-slate-200/80 dark:border-slate-800/60"
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          {/* Brand Logo */}
          <Link 
            href="/" 
            className="flex items-center gap-3 group focus:outline-none focus-visible:ring-2 focus-visible:ring-sky-500 rounded-lg"
          >
            <Image
              src={getAssetPath("/icons/Icon-512.png")}
              alt="RangoonX"
              width={40}
              height={40}
              className="w-10 h-10 object-contain transition-transform group-hover:scale-105"
              priority
            />
            <div className="flex flex-col">
              <span className="text-xl font-black tracking-tight text-slate-950 dark:text-white">
                {t("brand_name", "RangoonX")}
              </span>
              <span className="text-[10px] uppercase tracking-wider font-bold text-sky-700 dark:text-sky-400">
                Software House
              </span>
            </div>
          </Link>

          {/* Desktop Navigation Links - Clean Text with Active Bar */}
          <nav className="hidden md:flex items-center gap-6 lg:gap-8">
            {navLinks.map((link) => {
              const isActive = pathname === link.href;
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  className={`group relative py-2 text-base transition-colors duration-200 cursor-pointer ${
                    isActive
                      ? "text-sky-600 dark:text-sky-400 font-bold"
                      : "text-slate-800 dark:text-slate-300 hover:text-sky-600 dark:hover:text-white font-medium"
                  }`}
                >
                  <span>{t(link.labelKey)}</span>
                  
                  {/* Bottom Active Bar */}
                  {isActive ? (
                    <span className="absolute -bottom-1 left-0 right-0 h-0.5 bg-sky-600 dark:bg-sky-400 rounded-full shadow-xs shadow-sky-500/50" />
                  ) : (
                    <span className="absolute -bottom-1 left-0 right-0 h-0.5 bg-transparent group-hover:bg-slate-300 dark:group-hover:bg-slate-700 transition-colors rounded-full" />
                  )}
                </Link>
              );
            })}
          </nav>

          {/* Right Controls: Language, Theme, Contact CTA */}
          <div className="hidden md:flex items-center gap-3">
            {/* Language Switcher */}
            <button
              onClick={toggleLanguage}
              type="button"
              className="flex items-center gap-1.5 px-3 py-2 text-xs font-bold rounded-xl text-slate-800 dark:text-slate-100 bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 border-2 border-slate-300 dark:border-slate-700 transition-colors cursor-pointer shadow-sm"
              title="Switch Language"
            >
              <Globe className="w-4 h-4 text-sky-600 dark:text-sky-400" />
              <span>{language === "mm" ? "English" : "မြန်မာ"}</span>
            </button>

            {/* Theme Toggle */}
            <button
              onClick={toggleTheme}
              type="button"
              className="p-2.5 rounded-xl text-slate-800 dark:text-slate-100 bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 border-2 border-slate-300 dark:border-slate-700 transition-colors cursor-pointer shadow-sm"
              title="Toggle Theme"
              aria-label="Toggle Theme"
            >
              {theme === "dark" ? (
                <Sun className="w-4 h-4 text-amber-400" />
              ) : (
                <Moon className="w-4 h-4 text-slate-800" />
              )}
            </button>

            {/* Contact Sales / Get in Touch CTA */}
            <Link
              href="/contact"
              className="flex items-center gap-2 px-5 py-2.5 text-sm font-bold text-white bg-sky-600 hover:bg-sky-500 rounded-xl shadow-md hover:shadow-sky-500/30 transition-all duration-200 hover:-translate-y-0.5 cursor-pointer"
            >
              <span>{t("contact_sales", "Contact Sales")}</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <div className="flex md:hidden items-center gap-2">
            <button
              onClick={toggleLanguage}
              type="button"
              className="px-2.5 py-1.5 text-xs font-bold rounded-lg border-2 border-slate-300 dark:border-slate-700 text-slate-900 dark:text-slate-100 bg-white dark:bg-slate-900 shadow-xs"
            >
              {language === "mm" ? "EN" : "မြန်မာ"}
            </button>
            <button
              onClick={toggleTheme}
              type="button"
              className="p-2 rounded-lg border-2 border-slate-300 dark:border-slate-700 text-slate-900 dark:text-slate-100 bg-white dark:bg-slate-900 shadow-xs"
              aria-label="Toggle Theme"
            >
              {theme === "dark" ? (
                <Sun className="w-4 h-4 text-amber-400" />
              ) : (
                <Moon className="w-4 h-4 text-slate-800" />
              )}
            </button>
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              type="button"
              className="p-2 rounded-lg text-slate-900 dark:text-white bg-slate-100 dark:bg-slate-800 border-2 border-slate-300 dark:border-slate-700 shadow-xs"
              aria-label="Open menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Drawer Navigation */}
      {mobileMenuOpen && (
        <div className="md:hidden border-b-2 border-slate-300 dark:border-slate-800 bg-white dark:bg-[#070b12] px-4 pt-3 pb-6 space-y-3 shadow-2xl">
          <div className="flex flex-col space-y-1 px-2">
            {navLinks.map((link) => {
              const isActive = pathname === link.href;
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  onClick={() => setMobileMenuOpen(false)}
                  className={`relative py-3 px-2 text-base transition-colors ${
                    isActive
                      ? "text-sky-600 dark:text-sky-400 font-bold"
                      : "text-slate-800 dark:text-slate-200 hover:text-sky-600 font-medium"
                  }`}
                >
                  <span>{t(link.labelKey)}</span>
                  {isActive && (
                    <span className="absolute bottom-1 left-2 w-8 h-0.5 bg-sky-600 dark:bg-sky-400 rounded-full" />
                  )}
                </Link>
              );
            })}
          </div>
          <div className="pt-2">
            <Link
              href="/contact"
              onClick={() => setMobileMenuOpen(false)}
              className="w-full flex items-center justify-center gap-2 py-3.5 px-4 text-sm font-bold text-white bg-sky-600 hover:bg-sky-500 rounded-xl text-center shadow-md"
            >
              <span>{t("contact_sales", "Contact Sales")}</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      )}
    </header>
  );
}
