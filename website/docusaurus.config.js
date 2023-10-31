// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github')
const darkCodeTheme = require('prism-react-renderer/themes/dracula')

/** @type {import('@docusaurus/types').Config} */
const config = {
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
            /** @type {import('@docusaurus/preset-classic').Options} */
            ({
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
            }),
        ],
    ],

    themeConfig:
        /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
            // Replace with your project's social card
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
                        href: 'https://github.com/Nikilireous/irasshaimase-to-polytech',
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
                                href: 'https://github.com/Nikilireous/irasshaimase-to-polytech',
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
                theme: lightCodeTheme,
                darkTheme: darkCodeTheme,
            },
        }),
}

module.exports = config
