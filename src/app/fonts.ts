import localFont from "next/font/local";
import { Inter } from "next/font/google";

export const padauk = localFont({
  src: [
    {
      path: "../../public/fonts/Padauk-Regular.ttf",
      weight: "400",
      style: "normal",
    },
    {
      path: "../../public/fonts/Padauk-Bold.ttf",
      weight: "700",
      style: "normal",
    },
  ],
  variable: "--font-padauk",
  display: "swap",
});

export const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});
