// client/app/page.js

import Link from 'next/link';

// This function runs on the server at build or request time
async function getListings() {
  // Replace with your Django backend URL if needed
  const res = await fetch('http://localhost:8000/api/listings/', { cache: 'no-store' });
  if (!res.ok) {
    throw new Error('Failed to fetch listings');
  }
  return res.json();
}

export default async function HomePage() {
  const listings = await getListings();

  return (
    <div>
      <h2 className="text-3xl font-bold mb-4">Search Results</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {listings.map((listing) => (
          <Link
            key={listing.id}
            href={`/listing/${listing.id}`}
            className="border rounded-lg p-4 hover:shadow-lg transition"
          >
            {listing.image_urls && listing.image_urls.length > 0 && (
              <img
                src={listing.image_urls[0]}
                alt={listing.title}
                className="w-full h-48 object-cover mb-2 rounded"
              />
            )}
            <h3 className="text-xl font-semibold">{listing.title}</h3>
            <p className="text-gray-600">{listing.location}</p>
            <p className="mt-2 text-lg font-bold">
              ${listing.price_per_night} per night
            </p>
            <p className="text-sm text-gray-500">
              {listing.ratings} ★ ({listing.reviews} reviews)
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}
