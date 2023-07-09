import { ReactNode } from "react";
import Header from "./components/Header";
import { Providers } from "./providers";

type Props = { children: ReactNode };

const Layout = ({ children }: Props) => {
  return (
    <Providers>
      <Header />
      {children}
    </Providers>
  );
};

export default Layout;
