import * as React from 'react'
import Link from 'next/link';
import Image from 'next/image'
import styles from './header.module.css'

const Header = () => {
  return (
    <header className="border-b flex items-center h-14 px-4">
      <div  className={styles.logo}>
      <Image
              src="/rogo2.svg"
              alt="Logo"
              width={80}
              height={80}
              priority
      />
      <h1>
        PETAPETA
      </h1>
      </div>

      <div  className={styles.menu}>
      <Link href="/">
      <Image
              src="/home2.svg"
              alt="Logo"
              width={60}
              height={60}
              priority
      />
      </Link>
      <h1>
      ホーム
      </h1>

      <Link href="/">
      <Image
              src="/toukou2.svg"
              alt="Logo"
              width={60}
              height={60}
              priority
      />
      </Link>
      <h1>
      投稿
      </h1>

      

    </div>
    </header>
  );
};

export default Header;