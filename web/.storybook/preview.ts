import type { Preview } from '@storybook/html'
import '../src/main'

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on[A-Z].*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/
      }
    },
    backgrounds: {
      default: 'White',
      values: [
        { name: 'light grey', value: '#E3E8EE' },
        { name: 'White', value: '#fff' }
      ]
    }
  }
}

export default preview
