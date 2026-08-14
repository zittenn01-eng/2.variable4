import { NextResponse } from "next/server";
import path from "path";
import fs from "fs";

const PIZZA_FILE = path.join(process.cwd(), "pizza.py");

export async function GET() {
  try {
    const code = fs.readFileSync(PIZZA_FILE, "utf-8");
    return NextResponse.json({ code });
  } catch {
    return NextResponse.json({ code: null, error: "File not found" }, { status: 404 });
  }
}

export async function POST(req: Request) {
  try {
    const { code } = await req.json();
    fs.writeFileSync(PIZZA_FILE, code, "utf-8");
    return NextResponse.json({ ok: true });
  } catch {
    // Read-only filesystem (e.g. Vercel) — silently ignore
    return NextResponse.json({ ok: false, error: "Read-only filesystem" }, { status: 200 });
  }
}
