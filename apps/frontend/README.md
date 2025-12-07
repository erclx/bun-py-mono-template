# Bun-Py Frontend

The React frontend for the Bun-Py Monorepo. Built with **React 19**, **Vite**, **Bun**, and **Tailwind CSS**.

## Disclaimer

This is opinionated. Use what works for you, ignore the rest, and stay consistent with your own choices.

## What's Included

### Core Stack
- **Bun**: Runtime and package manager
- **React 19**: Latest React with **Vite** for fast development
- **TypeScript**: Strict type safety
- **Tailwind CSS v4**: Utility-first styling

### Testing
- **Vitest**: Blazing fast unit and integration tests
- **React Testing Library**: Component testing
- **Happy DOM**: Lightweight browser environment simulation

### Code Quality
- **ESLint**: Includes accessibility checks, import sorting, and kebab-case file naming
- **Prettier**: Code formatting with Tailwind class sorting

## Quick Start

```bash
cd apps/frontend
bun install
bun run dev
```

## Scripts

```bash
bun run dev            # Start development server (opens browser)
bun run build          # Type check and build for production
bun run lint           # Auto-fix linting issues
bun test               # Run tests
bun run test:ui        # Run tests with interactive UI
bun run test:coverage  # Run tests with coverage report
```

## Project Conventions

### Absolute Imports

Use `@/*` to import from `src`. Avoid `../` paths.

* Good: `import { Button } from '@/components/ui/button'`
* Bad: `import { Button } from '../../components/ui/button'`

### File Naming

All files and folders in `src` must be kebab-case (e.g., `theme-toggle.tsx`). ESLint enforces this.

* File: `theme-toggle.tsx`
* Component: `export function ThemeToggle() {...}`

### Testing

Test files use the `.test.tsx` or `.test.ts` extension.

* Test file: `theme-toggle.test.tsx`
* Location: Co-located with the component or in `__tests__` folders

## Structure

```text
apps/frontend/
├── src/
│   ├── app/           # App-wide logic (routes, providers)
│   ├── components/    # Shared components (ui, layouts)
│   ├── features/      # Feature-based modules
│   ├── hooks/         # Custom React hooks
│   ├── lib/           # External library configurations
│   ├── testing/       # Test setup and utilities
│   └── utils/         # Stateless utility functions
├── bunfig.toml        # Bun config
├── vite.config.ts     # Vite config
└── vitest.config.ts   # Vitest config
```

## Credits

Architecture inspired by Bulletproof React.
