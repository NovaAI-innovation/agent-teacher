import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  // Note: Tailwind CSS v4 uses CSS-based configuration via @theme in globals.css
  // This config file is maintained for compatibility and tooling support
};

export default config;
