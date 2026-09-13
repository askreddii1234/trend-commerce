import Link from "next/link";
import { notFound } from "next/navigation";
import { getTrend } from "@/lib/api";
import GenerationForm from "./GenerationForm";

export default async function TrendPage({ params }: { params: Promise<{slug:string}> }) {
  const { slug } = await params;
  const trend = await getTrend(slug);
  const fallback = slug === "retro-80s-india" ? {slug,title:"80s India Portrait",eyebrow:"Trending in India",description:"Upload a portrait and see yourself reimagined with warm 1980s Indian studio styling.",is_free:true,price_inr:0,category:"image",badge:"Free launch",variants:[{id:"classic",label:"Classic Studio"},{id:"bollywood",label:"Cinema Glam"},{id:"kerala",label:"Kerala Retro"},{id:"saree",label:"Retro Saree"}]} : null;
  const data = trend || fallback;
  if (!data) notFound();
  return <main className="shell"><nav className="nav"><Link className="brand" href="/">TrendDrop</Link><div className="pill">Free launch</div></nav><section className="detail"><div className="panel"><div className="badge">🔥 {data.badge}</div><div className="small">{data.eyebrow}</div><h1>{data.title}</h1><p>{data.description}</p><h3>Built for sharing</h3><p className="small">We preserve your identity while applying a generic period aesthetic. We do not imitate a specific celebrity or copyrighted movie character.</p></div><GenerationForm trend={data}/></section></main>;
}
