"use client";

import { useRouter } from "next/navigation";

type props = {
  path: string;
  children: React.ReactNode;
};

function Button(props: props) {
  const router = useRouter();
  const handleClick = (e: any) => {
    e.preventDefault();
    router.push(props.path);
  };
  return <button onClick={handleClick}>{props.children}</button>;
}

export default Button;
