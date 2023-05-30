import type { StoryObj, Meta } from '@storybook/html'
import { INITIAL_VIEWPORTS } from '@storybook/addon-viewport'
import { Link } from './types'

type Props = {
  links: Link[]
  activeLink: string
}

const links = [
  { text: 'Home', href: '#' },
  { text: 'Food', href: '#' },
  { text: 'Fruit', href: '#' }
]

/**
 * The ETF header with navigation and user account controls.
 */
const meta = {
  title: 'Components/Breadcrumb',
  tags: ['autodocs'],
  render: ({ links, activeLink }) =>
    `
    <nav aria-label="Breadcrumb" class="breadcrumb">
    <ol>
      ${
        links &&
        links.map(({ text, href }) => `<li><a href="${href}">${text}</a></li>`).join('')
      }
      ${activeLink ? `<li aria-current="true">${activeLink}</li>` : ''}
      
    </ol>
  </nav>

   
    `,
  argTypes: {},
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=485-752&t=lsxxoIbrtlv60JJm-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Breadcrumb: Story = {
  args: {
    links,
    activeLink: 'Apples'
  }
}
