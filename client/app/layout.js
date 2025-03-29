// client/app/layout.js

import './globals.css';

export const metadata = {
  title: 'Airbnb Clone',
  description: 'A Next.js Airbnb clone built with Tailwind CSS',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-50">
        <header className="bg-white shadow py-4">
          <div className="container mx-auto flex justify-between items-center px-4">
            <h1 className="text-2xl font-bold text-red-600">Airbnb Clone</h1>
            {/* Optional: Add navigation or a search bar here */}
          </div>
        </header>
        <main className="container mx-auto p-4">{children}</main>
        <footer className="bg-gray-100 py-4 mt-8">
          <div className="container mx-auto text-center text-gray-600">
            &copy; {new Date().getFullYear()} Airbnb Clone. All rights reserved.
          </div>
        </footer>
      </body>
    </html>
  );
}
