"use client";

import React, { useState } from "react";
import { useLanguage } from "@/context/LanguageContext";
import companyInfo from "@/data/company_info.json";
import { 
  Mail, 
  Phone, 
  MapPin, 
  MessageSquare, 
  Send, 
  CheckCircle2, 
  ArrowUpRight, 
  Loader2 
} from "lucide-react";

export default function ContactForm() {
  const { t } = useLanguage();

  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    interest: "form_interest_opt1",
    message: "",
  });

  const [status, setStatus] = useState<"idle" | "submitting" | "success" | "error">("idle");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.firstName.trim() || !formData.email.trim() || !formData.message.trim()) {
      setErrorMessage(t("form_required_error", "Please fill in all required fields."));
      return;
    }

    setErrorMessage("");
    setStatus("submitting");

    const interestLabels: Record<string, string> = {
      form_interest_opt1: "Custom Software Development (စိတ်ကြိုက် Software ရေးဆွဲခြင်း)",
      form_interest_opt2: "Cloud Infrastructure & Migration (Cloud စနစ် တည်ဆောက်ခြင်း)",
      form_interest_opt3: "AI & Machine Learning Integration (AI ပေါင်းစပ်ခြင်း)",
      form_interest_opt4: "Enterprise POS / ERP Solution (လုပ်ငန်းသုံး POS / ERP စနစ်)",
      form_interest_opt5: "Other Inquiry (အခြား မေးမြန်းချက်များ)",
    };

    const fullName = `${formData.firstName} ${formData.lastName}`.trim();
    const serviceName = interestLabels[formData.interest] || formData.interest;

    try {
      const web3FormsKey = process.env.NEXT_PUBLIC_WEB3FORMS_ACCESS_KEY;
      let response: Response;

      if (web3FormsKey) {
        response = await fetch("https://api.web3forms.com/submit", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            access_key: web3FormsKey,
            subject: `RangoonX New Inquiry: ${fullName} (${serviceName})`,
            name: fullName,
            email: formData.email,
            service: serviceName,
            message: formData.message,
            from_name: "RangoonX Website",
          }),
        });
      } else {
        response = await fetch(`https://formsubmit.co/ajax/${companyInfo.email}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            _subject: `RangoonX New Inquiry: ${fullName} (${serviceName})`,
            _template: "table",
            _captcha: "false",
            _replyto: formData.email,
            "Full Name": fullName,
            "Client Email": formData.email,
            "Interested Service": serviceName,
            "Project Details": formData.message,
            "Submitted At": new Date().toLocaleString(),
          }),
        });
      }

      const result = await response.json();

      if (response.ok && (result.success === "true" || result.success === true || result.success === undefined)) {
        setStatus("success");
      } else if (result.message && result.message.includes("Activation")) {
        setStatus("success");
      } else {
        throw new Error(result.message || "Failed to submit inquiry");
      }
    } catch (err) {
      console.error("Inquiry submission error:", err);
      setErrorMessage(
        t(
          "form_error",
          "မေးမြန်းချက် ပေးပို့ရာတွင် အဆင်မပြေမှု ဖြစ်ပေါ်နေပါသည်။ အောက်ပါ အီးမေးလ် သို့မဟုတ် ဖုန်းနံပါတ်သို့ တိုက်ရိုက် ဆက်သွယ်ပေးပို့နိုင်ပါသည်။"
        )
      );
      setStatus("error");
    }
  };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
      {/* Left Column: Direct Info & Office */}
      <div className="lg:col-span-5 space-y-8">
        <div>
          <h2 className="text-2xl font-black tracking-tight text-slate-950 dark:text-white mb-3">
            {t("contact_hq_title", "HQ Office")}
          </h2>
          <p className="text-slate-800 dark:text-slate-200 text-sm sm:text-base leading-relaxed font-normal">
            {t("contact_page_subtitle", "Reach out to discuss custom software solutions, cloud migrations, or how we can integrate AI into your workflow.")}
          </p>
        </div>

        {/* Contact Detail Cards */}
        <div className="space-y-4">
          {/* HQ Address */}
          <a
            href={companyInfo.maps_url}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-start gap-4 p-4 rounded-xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 hover:border-sky-500 dark:hover:border-sky-500 transition-all group shadow-sm"
          >
            <div className="w-11 h-11 rounded-lg bg-rose-100 dark:bg-rose-950/70 border border-rose-300 dark:border-rose-500/40 flex items-center justify-center text-rose-600 dark:text-rose-400 shrink-0 mt-0.5 shadow-sm">
              <MapPin className="w-5 h-5" />
            </div>
            <div className="flex-1">
              <span className="text-xs font-mono font-bold uppercase text-slate-700 dark:text-slate-400 block mb-1">
                {t("contact_hq_title", "Location")}
              </span>
              <p className="text-sm font-bold text-slate-950 dark:text-white group-hover:text-sky-600 dark:group-hover:text-sky-400 transition-colors">
                {companyInfo.address}
              </p>
            </div>
            <ArrowUpRight className="w-4 h-4 text-slate-500 group-hover:text-sky-600 transition-colors shrink-0" />
          </a>

          {/* Email */}
          <a
            href={companyInfo.email_url}
            className="flex items-center gap-4 p-4 rounded-xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 hover:border-sky-500 dark:hover:border-sky-500 transition-all group shadow-sm"
          >
            <div className="w-11 h-11 rounded-lg bg-sky-100 dark:bg-sky-950 border border-sky-300 dark:border-sky-500/40 flex items-center justify-center text-sky-600 dark:text-sky-400 shrink-0 shadow-sm">
              <Mail className="w-5 h-5" />
            </div>
            <div className="flex-1">
              <span className="text-xs font-mono font-bold uppercase text-slate-700 dark:text-slate-400 block mb-0.5">
                {t("contact_email_title", "Email")}
              </span>
              <p className="text-sm font-bold text-slate-950 dark:text-white group-hover:text-sky-600 dark:group-hover:text-sky-400 transition-colors">
                {companyInfo.email}
              </p>
            </div>
            <ArrowUpRight className="w-4 h-4 text-slate-500 group-hover:text-sky-600 transition-colors shrink-0" />
          </a>

          {/* Direct Phone */}
          <a
            href={companyInfo.phone_url}
            className="flex items-center gap-4 p-4 rounded-xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 hover:border-sky-500 dark:hover:border-sky-500 transition-all group shadow-sm"
          >
            <div className="w-11 h-11 rounded-lg bg-emerald-100 dark:bg-emerald-950 border border-emerald-300 dark:border-emerald-500/40 flex items-center justify-center text-emerald-600 dark:text-emerald-400 shrink-0 shadow-sm">
              <Phone className="w-5 h-5" />
            </div>
            <div className="flex-1">
              <span className="text-xs font-mono font-bold uppercase text-slate-700 dark:text-slate-400 block mb-0.5">
                {t("contact_phone_title", "Phone")}
              </span>
              <p className="text-sm font-bold text-slate-950 dark:text-white group-hover:text-sky-600 dark:group-hover:text-sky-400 transition-colors">
                {companyInfo.phone}
              </p>
            </div>
            <ArrowUpRight className="w-4 h-4 text-slate-500 group-hover:text-sky-600 transition-colors shrink-0" />
          </a>

          {/* Viber Chat */}
          <a
            href={companyInfo.viber_url}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-4 p-4 rounded-xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 hover:border-sky-500 dark:hover:border-sky-500 transition-all group shadow-sm"
          >
            <div className="w-11 h-11 rounded-lg bg-purple-100 dark:bg-purple-950 border border-purple-300 dark:border-purple-500/40 flex items-center justify-center text-purple-600 dark:text-purple-400 shrink-0 shadow-sm">
              <MessageSquare className="w-5 h-5" />
            </div>
            <div className="flex-1">
              <span className="text-xs font-mono font-bold uppercase text-slate-700 dark:text-slate-400 block mb-0.5">
                {t("contact_viber_title", "Viber Official")}
              </span>
              <p className="text-sm font-bold text-slate-950 dark:text-white group-hover:text-sky-600 dark:group-hover:text-sky-400 transition-colors">
                {companyInfo.viber}
              </p>
            </div>
            <ArrowUpRight className="w-4 h-4 text-slate-500 group-hover:text-sky-600 transition-colors shrink-0" />
          </a>
        </div>
      </div>

      {/* Right Column: Interactive Consultation Form */}
      <div className="lg:col-span-7">
        <div className="p-8 sm:p-10 rounded-2xl border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 shadow-xl">
          {status === "success" ? (
            <div className="text-center py-12 space-y-4">
              <div className="w-16 h-16 rounded-full bg-emerald-100 dark:bg-emerald-950 border-2 border-emerald-500 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mx-auto shadow-sm">
                <CheckCircle2 className="w-8 h-8" />
              </div>
              <h3 className="text-2xl font-black text-slate-950 dark:text-white">
                {t("form_inquiry_received", "Inquiry Received")}
              </h3>
              <p className="text-slate-800 dark:text-slate-200 max-w-md mx-auto text-sm sm:text-base leading-relaxed font-normal">
                {t("form_success", "Thank you for reaching out! Our engineering team will review your inquiry and get back to you within 24 hours.")}
              </p>
              <div className="pt-4">
                <button
                  onClick={() => {
                    setStatus("idle");
                    setFormData({
                      firstName: "",
                      lastName: "",
                      email: "",
                      interest: "form_interest_opt1",
                      message: "",
                    });
                  }}
                  className="px-6 py-2.5 rounded-lg text-sm font-bold bg-sky-600 text-white hover:bg-sky-500 transition-colors shadow-md cursor-pointer"
                >
                  {t("form_send_another", "Send Another Inquiry")}
                </button>
              </div>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {/* First Name */}
                <div className="space-y-2">
                  <label className="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-slate-100">
                    {t("form_first_name", "First Name")} <span className="text-rose-600 dark:text-rose-400">*</span>
                  </label>
                  <input
                    type="text"
                    required
                    value={formData.firstName}
                    onChange={(e) => setFormData({ ...formData, firstName: e.target.value })}
                    className="w-full px-4 py-3 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-950 dark:text-white placeholder-slate-400 focus:outline-none focus:border-sky-500 text-sm transition-all font-medium"
                    placeholder="e.g. Aung"
                  />
                </div>

                {/* Last Name */}
                <div className="space-y-2">
                  <label className="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-slate-100">
                    {t("form_last_name", "Last Name")}
                  </label>
                  <input
                    type="text"
                    value={formData.lastName}
                    onChange={(e) => setFormData({ ...formData, lastName: e.target.value })}
                    className="w-full px-4 py-3 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-950 dark:text-white placeholder-slate-400 focus:outline-none focus:border-sky-500 text-sm transition-all font-medium"
                    placeholder="e.g. Kyaw"
                  />
                </div>
              </div>

              {/* Work Email */}
              <div className="space-y-2">
                <label className="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-slate-100">
                  {t("form_email", "Work Email")} <span className="text-rose-600 dark:text-rose-400">*</span>
                </label>
                <input
                  type="email"
                  required
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="w-full px-4 py-3 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-950 dark:text-white placeholder-slate-400 focus:outline-none focus:border-sky-500 text-sm transition-all font-medium"
                  placeholder="name@company.com"
                />
              </div>

              {/* Area of Interest */}
              <div className="space-y-2">
                <label className="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-slate-100">
                  {t("form_interest", "Area of Interest")}
                </label>
                <select
                  value={formData.interest}
                  onChange={(e) => setFormData({ ...formData, interest: e.target.value })}
                  className="w-full px-4 py-3 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-950 dark:text-white focus:outline-none focus:border-sky-500 text-sm transition-all font-medium"
                >
                  <option value="form_interest_opt1">{t("form_interest_opt1", "Custom Software Development")}</option>
                  <option value="form_interest_opt2">{t("form_interest_opt2", "Cloud Infrastructure & Migration")}</option>
                  <option value="form_interest_opt3">{t("form_interest_opt3", "AI & Machine Learning Integration")}</option>
                  <option value="form_interest_opt4">{t("form_interest_opt4", "Enterprise POS / ERP Solution")}</option>
                  <option value="form_interest_opt5">{t("form_interest_opt5", "Other Inquiry")}</option>
                </select>
              </div>

              {/* Message */}
              <div className="space-y-2">
                <label className="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-slate-100">
                  {t("form_message", "Project Details")} <span className="text-rose-600 dark:text-rose-400">*</span>
                </label>
                <textarea
                  required
                  rows={4}
                  value={formData.message}
                  onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                  className="w-full px-4 py-3 rounded-lg border-2 border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-950 dark:text-white placeholder-slate-400 focus:outline-none focus:border-sky-500 text-sm transition-all resize-y font-medium"
                  placeholder={t("form_message_placeholder", "Tell us about your project requirements, timeline, and goals...")}
                />
              </div>

              {errorMessage && (
                <div className="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/40 border-2 border-rose-300 dark:border-rose-800 text-rose-700 dark:text-rose-300 text-xs sm:text-sm space-y-2">
                  <p className="font-semibold">{errorMessage}</p>
                  <div className="flex flex-wrap items-center gap-3 pt-1 text-xs">
                    <a
                      href={`mailto:${companyInfo.email}?subject=Inquiry from ${encodeURIComponent(formData.firstName)}&body=${encodeURIComponent(formData.message)}`}
                      className="inline-flex items-center gap-1 font-bold text-sky-700 dark:text-sky-400 hover:underline"
                    >
                      <Mail className="w-3.5 h-3.5" />
                      Email ဖြင့် တိုက်ရိုက်ပို့ရန်
                    </a>
                    <span className="text-slate-400">•</span>
                    <a
                      href={companyInfo.viber_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1 font-bold text-purple-700 dark:text-purple-400 hover:underline"
                    >
                      <MessageSquare className="w-3.5 h-3.5" />
                      Viber ဖြင့် ဆက်သွယ်ရန်
                    </a>
                  </div>
                </div>
              )}

              {/* Submit Button */}
              <button
                type="submit"
                disabled={status === "submitting"}
                className="w-full py-4 px-6 rounded-xl font-bold text-white bg-sky-600 hover:bg-sky-500 disabled:opacity-50 transition-all flex items-center justify-center gap-2 cursor-pointer shadow-lg shadow-sky-600/30"
              >
                {status === "submitting" ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>{t("form_submitting", "Sending...")}</span>
                  </>
                ) : (
                  <>
                    <span>{t("form_submit", "Send Inquiry")}</span>
                    <Send className="w-4 h-4" />
                  </>
                )}
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
