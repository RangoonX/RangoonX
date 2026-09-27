"use client";

import React from "react";
import Hero from "@/components/Hero";
import TechStackMarquee from "@/components/TechStackMarquee";
import CapabilitiesSection from "@/components/CapabilitiesSection";
import WhyUs from "@/components/WhyUs";
import CtaBanner from "@/components/CtaBanner";

export default function HomePage() {
  return (
    <div className="space-y-6">
      <Hero />
      <TechStackMarquee />
      <CapabilitiesSection />
      <WhyUs />
      <CtaBanner />
    </div>
  );
}
