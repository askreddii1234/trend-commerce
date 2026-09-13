"use client";
import { FormEvent, useState } from "react";
import { API_BASE, TrendProduct } from "@/lib/api";

export default function GenerationForm({ trend }: { trend: TrendProduct }) {
  const [file, setFile] = useState<File | null>(null);
  const [variant, setVariant] = useState(trend.variants?.[0]?.id || "classic");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<string | null>(null);

  async function submit(e: FormEvent) {
    e.preventDefault(); setError(""); setResult(null);
    if (!file) { setError("Choose a clear portrait first."); return; }
    const body = new FormData(); body.append("product_slug", trend.slug); body.append("variant", variant); body.append("image", file); body.append("source", "web");
    setBusy(true);
    try {
      const res = await fetch(`${API_BASE}/generations/`, { method: "POST", body });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Generation failed");
      setResult(data.result_url);
    } catch (err) { setError(err instanceof Error ? err.message : "Generation failed"); }
    finally { setBusy(false); }
  }

  return <form className="panel" onSubmit={submit}>
    <h2>Make yours</h2>
    <div className="drop"><input type="file" accept="image/jpeg,image/png,image/webp" onChange={(e)=>setFile(e.target.files?.[0] || null)} /><p className="small">Use a clear portrait. Max 10MB.</p></div>
    <label className="small">Style</label>
    <select className="input" value={variant} onChange={(e)=>setVariant(e.target.value)}>{trend.variants?.map(v=><option value={v.id} key={v.id}>{v.label}</option>)}</select>
    <button className="button" disabled={busy}>{busy ? "Creating…" : "Generate free"}</button>
    <p className="small">One free generation per person/day during launch. Uploaded photos are used only to create your result.</p>
    {error && <p>{error}</p>}
    {result && <div className="result"><h3>Your 80s portrait</h3><img src={result} alt="Generated retro portrait"/><a className="cta" href={result} target="_blank" rel="noreferrer">Open & download</a></div>}
  </form>;
}
