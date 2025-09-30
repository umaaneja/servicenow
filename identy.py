  import sailpoint.object.Identity;
    import sailpoint.object.Link;


Identity identity = context.getObjectByName(Identity.class, identityName);
    if (identity == null) {
        System.out.println("❌ Identity not found: " + identityName);
    } else {
        for (Link link : identity.getLinks()) {
            if (link.getApplicationName().equalsIgnoreCase(appName)) {
                System.out.println("✅ Azure AD nativeIdentity = " + link.getNativeIdentity());
            }
        }
    }
