import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "TrendDrop — AI trends you can try now",
  description: "Free personalized AI trend experiences made for sharing.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en-IN"><body>{children}</body></html>;
}
