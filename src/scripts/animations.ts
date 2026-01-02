import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!prefersReducedMotion) {
	gsap.registerPlugin(ScrollTrigger);
	const revealStart = "top 92%";
	const revealEase = "power3.out";

	const animateReveal = (
		targets: gsap.TweenTarget,
		options: { duration: number; stagger?: number }
	) => {
		gsap.to(
			targets,
			{
				y: 0,
				autoAlpha: 1,
				duration: options.duration,
				ease: revealEase,
				stagger: options.stagger
			}
		);
	};

	const hero = document.querySelector<HTMLElement>("[data-hero]");
	if (hero) {
		const heroItems = hero.querySelectorAll<HTMLElement>("[data-hero-item]");
		gsap
			.timeline({ defaults: { duration: 0.9, ease: revealEase } })
			.to(heroItems, {
				y: 0,
				autoAlpha: 1,
				stagger: 0.12
			});

		const heroLogo = hero.querySelector<HTMLElement>("[data-hero-logo]");
		if (heroLogo) {
			gsap.to(heroLogo, {
				y: -6,
				duration: 3.2,
				ease: "sine.inOut",
				repeat: -1,
				yoyo: true
			});
		}
	}

	ScrollTrigger.batch("[data-reveal]", {
		start: revealStart,
		once: true,
		onEnter: (batch) => {
			animateReveal(batch, { duration: 0.8, stagger: 0.08 });
		}
	});

	document.querySelectorAll<HTMLElement>("[data-reveal-stagger]").forEach((block) => {
		const items = Array.from(block.querySelectorAll<HTMLElement>("[data-reveal-item]"));
		if (!items.length) {
			return;
		}

		ScrollTrigger.create({
			trigger: block,
			start: revealStart,
			once: true,
			onEnter: () => {
				animateReveal(items, { duration: 0.7, stagger: 0.08 });
			}
		});
	});

	window.addEventListener("load", () => {
		ScrollTrigger.refresh();
	});
}
