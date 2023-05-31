import type { StoryObj, Meta } from '@storybook/html'
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
 * A progress bar to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/ProgressBar',
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
      url: 'https://www.figma.com/file/2ZaOCrzk941el36zvdgSHA/Evaluation-Registry?type=design&node-id=443-11663&t=myY59OmXjRW0K1yQ-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const ProgressBar: Story = {
  args: {
    links,
    activeLink: 'Apples'
  }
}
