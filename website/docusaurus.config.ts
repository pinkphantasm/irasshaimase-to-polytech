import type { Config } from '@docusaurus/types'
import type { Options, ThemeConfig } from '@docusaurus/preset-classic'
import { themes as prismThemes } from 'prism-react-renderer'

const config: Config = {
    title: 'Irasshaimase to Polytech',
    tagline: 'Прочувствуй Политех',
    favicon: 'img/favicon.ico',

    url: 'https://irasshaimase.shelepugin.ru',
    baseUrl: '/',

    organizationName: 'Pink Phantasm',
    projectName: 'irasshaimase-to-polytech',

    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'warn',

    i18n: {
        defaultLocale: 'ru',
        locales: ['en', 'ru'],
        localeConfigs: {
            en: {
                label: 'English',
            },
            ru: {
                htmlLang: 'ru',
                label: 'Русский',
            },
        },
    },

    presets: [
        [
            'classic',
            {
                docs: {
                    sidebarPath: require.resolve('./sidebars.js'),
                },
                blog: {
                    showReadingTime: true,
                },
                theme: {
                    customCss: require.resolve('./src/css/custom.css'),
                },
                sitemap: {
                    changefreq: 'weekly',
                    priority: 0.5,
                    ignorePatterns: ['/tags/**'],
                    filename: 'sitemap.xml',
                },
            } satisfies Options,
        ],
    ],

    themeConfig: {
        image: 'img/social-card.png',
        navbar: {
            title: 'Irasshaimase to Polytech',
            logo: {
                alt: 'Irasshaimase to Polytech',
                src: 'img/logo.png',
            },
            items: [
                {
                    type: 'docSidebar',
                    sidebarId: 'tutorialSidebar',
                    position: 'left',
                    label: 'Guide',
                },
                {
                    type: 'localeDropdown',
                    position: 'right',
                },
                {
                    href: 'https://github.com/Pink-Phantasm/irasshaimase-to-polytech',
                    label: 'GitHub',
                    position: 'right',
                },
            ],
        },
        footer: {
            style: 'dark',
            links: [
                {
                    title: 'Guide',
                    items: [
                        {
                            label: 'About',
                            to: '/docs/intro',
                        },
                        {
                            label: 'Installation',
                            to: '/docs/installation',
                        },
                    ],
                },
                {
                    title: 'More',
                    items: [
                        {
                            label: 'GitHub',
                            href: 'https://github.com/Pink-Phantasm/irasshaimase-to-polytech',
                        },
                        {
                            html: `
              <a href="https://www.netlify.com" target="_blank" rel="noreferrer noopener" aria-label="Deploys by Netlify">
                  <img src="https://www.netlify.com/img/global/badges/netlify-color-accent.svg" alt="Deploys by Netlify" width="114" height="51" />
              </a>`,
                        },
                    ],
                },
            ],
            copyright: `Copyright © ${new Date().getFullYear()} Pink Phantasm. Built with Docusaurus.`,
        },
        prism: {
            theme: prismThemes.github,
            darkTheme: prismThemes.dracula,
        },
    } satisfies ThemeConfig,
}

module.exports = config
