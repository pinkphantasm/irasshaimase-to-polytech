import React from 'react'
import clsx from 'clsx'
import Link from '@docusaurus/Link'
import Translate from '@docusaurus/Translate'
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'
import Layout from '@theme/Layout'

import styles from './index.module.css'

function HomepageHeader() {
    const { siteConfig } = useDocusaurusContext()
    return (
        <header className={clsx('hero hero--primary', styles.heroBanner)}>
            <div className="container">
                <img
                    className={styles.heroBannerLogo}
                    src="/img/irasshaimase-to-politech.png"
                    alt="Irasshaimase to Politech"
                />
                <h1 className="hero__title">{siteConfig.title}</h1>
                <p className="hero__subtitle">{siteConfig.tagline}</p>
                <div className={styles.buttons}>
                    <Link
                        className={clsx(
                            'button button--secondary button--lg',
                            styles.button,
                        )}
                        to="/docs/installation"
                    >
                        <Translate>⚙️ Installation</Translate>
                    </Link>
                    <Link
                        className={clsx(
                            'button button--secondary button--lg',
                            styles.button,
                        )}
                        to="/docs/plot"
                    >
                        <Translate>📕 Plot</Translate>
                    </Link>
                    <Link
                        className={clsx(
                            'button button--secondary button--lg',
                            styles.button,
                        )}
                        to="/docs/intro"
                    >
                        <Translate>⭐ About</Translate>
                    </Link>
                </div>
            </div>
        </header>
    )
}

function Intro(): JSX.Element {
    return (
        <section className={styles.intro}>
            <img
                className={styles.introCharacter}
                src="/img/sugaki.png"
                alt="Sugaki Kogu"
            />
            <blockquote>
                <h2>
                    <Translate>
                        Get to know the wonderful world of Politech!
                    </Translate>
                </h2>
                <p>
                    <Translate>
                        Learn about different directions of the university in a
                        playful way!
                    </Translate>
                </p>
            </blockquote>
        </section>
    )
}

function BeautifulLocations(): JSX.Element {
    return (
        <section className={styles.beautifulLocations}>
            <blockquote>
                <h2>
                    <Translate>Explore beautiful locations!</Translate>
                </h2>
                <p>
                    <Translate>
                        Feel yourself as a first year student eager for new
                        experiences!
                    </Translate>
                </p>
            </blockquote>
            <div className={styles.backgroundImageGroup}>
                <img src="/img/bg1.png" alt="Game background image" />
                <img src="/img/bg2.png" alt="Game background image" />
                <img src="/img/bg3.png" alt="Game background image" />
            </div>
        </section>
    )
}

export default function Home(): JSX.Element {
    const { siteConfig } = useDocusaurusContext()
    return (
        <Layout
            title={`Hello from ${siteConfig.title}`}
            description="Description will go into a meta tag in <head />"
        >
            <HomepageHeader />
            <main>
                <Intro />
                <BeautifulLocations />
            </main>
        </Layout>
    )
}
