import { defineConfig } from 'vite'
import postcssNesting from 'postcss-nesting'
import postcssCustomMedia from 'postcss-custom-media'
import svgLoader from 'vite-svg-loader'
// eslint-disable-next-line import/no-named-as-default
import liveReload from 'vite-plugin-live-reload'

export default defineConfig({
  server: {
    port: 5173
  },
  plugins: [
    svgLoader({ defaultImport: 'raw' }),
    liveReload('../etf/templates/**/*.*', { alwaysReload: true })
  ],
  css: {
    postcss: {
      plugins: [postcssNesting, postcssCustomMedia]
    }
  },
  build: {
    outDir: '../static/dist',
    rollupOptions: {
      output: {
        entryFileNames: `assets/[name].js`,
        chunkFileNames: `assets/[name].js`,
        assetFileNames: `assets/[name].[ext]`
      }
    }
  }
})
