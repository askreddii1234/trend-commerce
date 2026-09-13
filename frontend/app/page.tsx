import Link from "next/link";
import { getTrends } from "@/lib/api";

export default async function Home() {
  const trends = await getTrends();
  return <main className="shell">
    <nav className="nav"><div className="brand">TrendDrop</div><div className="pill">India launch • free</div></nav>
    <section className="hero"><h1>Try the internet&apos;s next trend before it gets old.</h1><p>Fast, personalized AI experiences built around what India is sharing right now. Upload once, create, download, share.</p></section>
    <section className="grid">
      {(trends.length ? trends : [{slug:"retro-80s-india",title:"80s India Portrait",eyebrow:"Trending in India",description:"See yourself reimagined as an authentic 1980s Indian studio portrait.",is_free:true,price_inr:0,category:"image",badge:"Free launch",variants:[]}]).map((trend)=><article className="card" key={trend.slug}>
        <div className="badge">🔥 {trend.badge || "Trending now"}</div><div className="small">{trend.eyebrow}</div><h2>{trend.title}</h2><p>{trend.description}</p><Link className="cta" href={`/trends/${trend.slug}`}>{trend.is_free ? "Create free" : `Try for ₹${trend.price_inr}`}</Link>
      </article>)}
    </section>
  </main>;
}
