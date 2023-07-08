# Installations

## frontend/Next

```PowerShell
> npm init 
> npx create-next-app petapeta --typescript
√ Would you like to use ESLint with this project? ... No / Yes
√ Would you like to use Tailwind CSS with this project? ... No / Yes
√ Would you like to use `src/` directory with this project? ... No / Yes
√ Use App Router (recommended)? ... No / Yes
√ Would you like to customize the default import alias? ... No / Yes
√ What import alias would you like configured? ... ~/*
Creating a new Next.js app in C:\Users\k0eov\Documents\KDDI_Hacks_2023\TeamE\KDDIHacks2023-TeamE\frontend\apps\petapeta.

Using npm.

Initializing project with template: app


Installing dependencies:
- react
- react-dom
- next
- typescript
- @types/react
- @types/node
- @types/react-dom
- eslint
- eslint-config-next


added 291 packages, and audited 292 packages in 41s

> node -v; npm -v; npx -v
v18.16.0
9.5.1
9.5.1


> npm install --save-dev recoil


```




# Notes

## 技術選定等

* 永続化には `recoil-persist` が使えるらしいが、何分ドキュメントが少なく、エラー報告も多いため、 `cookie` を使うことにする