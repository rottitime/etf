import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  level: number
}

/**
 * A progress bar to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/ProgressBar',
  tags: ['autodocs'],
  render: ({ level }) =>
    `
    <div class="progress-bar-horizontal-wide">
    ${[...Array(5).keys()]
      .map((i) => `<div class="square ${i < level ? 'filled' : ''}"></div>`)
      .join(``)}
      </div>

    `,
  argTypes: {
    level: {
      name: 'level',
      description: 'Number of squares filled in the progress bar',
      control: { type: 'range', min: 0, max: 5 }
    }
  },
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
    level: 2
  }
}
