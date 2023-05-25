import type { StoryObj, Meta } from '@storybook/html'
import { INITIAL_VIEWPORTS } from '@storybook/addon-viewport'
import { Link } from './types'

type Props = {
  title: string
  links: Link[]
  loggedIn: boolean
  primaryCta: string
  logout: string
}

const links = [...Array(3).keys()].map((i) => ({ text: `Link ${i}`, href: '#' }))

/**
 * The ETF header with navigation and user account controls.
 */
const meta = {
  title: 'Components/Header',
  tags: ['autodocs'],
  render: ({ links, title, loggedIn, primaryCta, logout }) =>
    `
      <header id="main-header">
        <div class="container">
          <a href="/" class="logo">
            <gov-icon key="crest"></gov-icon>
            <h2 class="body-text">${title}</h2>
          </a>

          ${
            loggedIn
              ? `
          <button id="main-header-mobile-menu">
            <span></span>
          </button>

          <nav id="main-header-menu">
            ${links.map(({ text, href }) => `<a href="${href}">${text}</a>`).join('')}

            <a class="bttn-primary" href="#">${primaryCta}</a>
            <a href="#">${logout}</a>
          </nav>`
              : ''
          }
        </div>
      </header>
    `,
  argTypes: {
    title: { control: 'text' },
    primaryCta: { control: 'text' },
    logout: { control: 'text' },
    loggedIn: { control: 'boolean', table: { disable: true } }
  },
  parameters: {
    viewpoert: {
      viewports: INITIAL_VIEWPORTS,
      defaultViewport: 'desktop'
    },
    backgrounds: {
      default: 'light grey'
    },
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-291&t=NMzWF77GnAa7BvPp-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    title: 'Evaluation Registry'
  }
}

export const Authenticated: Story = {
  args: {
    title: 'Evaluation Registry',
    primaryCta: 'Create an evaluation',
    logout: 'Logout',
    loggedIn: true,
    links
  }
}

export const Mobile: Story = {
  ...Authenticated,
  parameters: {
    viewport: {
      defaultViewport: 'mobile1'
    }
  }
}
