export const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api/v1";

export type TrendProduct = {
  slug: string; title: string; eyebrow: string; description: string; is_free: boolean;
  price_inr: number; category: string; badge: string; variants: {id:string;label:string}[];
};

export async function getTrends(): Promise<TrendProduct[]> {
  const res = await fetch(`${API_BASE}/trends/`, { cache: "no-store" });
  if (!res.ok) return [];
  return res.json();
}

export async function getTrend(slug: string): Promise<TrendProduct | null> {
  const res = await fetch(`${API_BASE}/trends/${slug}/`, { cache: "no-store" });
  if (!res.ok) return null;
  return res.json();
}
