import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  level: number
  type: 'progress-bar-horizontal-wide' | 'progress-bar-horizontal'
  maximum: number
}

/**
 * A progress bar to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/ProgressBar',
  tags: ['autodocs'],
  render: ({ level, type, maximum }) =>
    `
    <div class="${type}">
    ${[...Array(maximum).keys()]
      .map((i) => `<div class="square ${i < level ? 'filled' : ''}"></div>`)
      .join(``)}
      </div>

    `,
  argTypes: {
    maximum: {
      table: { disable: true }
    },
    level: {
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

export const Standard: Story = {
  args: {
    level: 2,
    type: 'progress-bar-horizontal-wide',
    maximum: 5
  }
}

export const Mini: Story = {
  args: {
    ...Standard.args,
    type: 'progress-bar-horizontal',
    maximum: 7
  },
  argTypes: {
    level: {
      control: { type: 'range', min: 0, max: 7 }
    }
  }
}
