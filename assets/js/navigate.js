
$(document).ready(function() {
    
    $("#nav_1").click(function() {
        var root_path = get_root_path();
        location.href = root_path;
    });

    $("#nav_2").click(function() {
        var root_path = get_root_path();
        location.href = root_path + "/publications";
    });

    initializeSubtitleSidebar();
    initializeMobileSidebarToggle();
});

function get_root_path() {
    var full_path = window.document.location.href;
    var words = full_path.split('/');
    var root_path = words[0] + '//' + words[2];
    return root_path;
}

function initializeSubtitleSidebar() {
    var subtitleList = document.getElementById("subtitle-list");
    var pageWrapper = document.querySelector(".page-wrapper");
    if (!subtitleList || !pageWrapper) {
        return;
    }

    var headings = pageWrapper.querySelectorAll("h2, h3");
    subtitleList.innerHTML = "";

    if (!headings.length) {
        var emptyItem = document.createElement("li");
        emptyItem.className = "subtitle-empty";
        emptyItem.textContent = "No subsections";
        subtitleList.appendChild(emptyItem);
    } else {
        for (var i = 0; i < headings.length; i++) {
            var heading = headings[i];
            if (!heading.id) {
                heading.id = createHeadingId(heading.textContent, i + 1);
            }

            var listItem = document.createElement("li");
            var levelClass = heading.tagName.toLowerCase() === "h3" ? "subtitle-level-3" : "subtitle-level-2";
            listItem.className = levelClass;

            var link = document.createElement("a");
            link.href = "#" + heading.id;
            link.textContent = heading.textContent;

            listItem.appendChild(link);
            subtitleList.appendChild(listItem);
        }
    }

    var topItem = document.createElement("li");
    topItem.className = "subtitle-level-2 subtitle-back-to-top";
    var topLink = document.createElement("a");
    topLink.href = "#page-top";
    topLink.textContent = "Back to top";
    topItem.appendChild(topLink);
    subtitleList.appendChild(topItem);
}

function createHeadingId(text, index) {
    var normalized = (text || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
    if (!normalized) {
        normalized = "section";
    }
    return normalized + "-" + index;
}

function initializeMobileSidebarToggle() {
    var hideButton = document.getElementById("subtitle-sidebar-hide");
    var showButton = document.getElementById("subtitle-sidebar-show");
    if (!hideButton || !showButton) {
        return;
    }

    var mediaQuery = window.matchMedia("(max-width: 992px)");
    var storageKey = "mobileSubtitleSidebarHidden";
    var isHidden = true;
    try {
        var savedState = window.localStorage.getItem(storageKey);
        isHidden = savedState === null ? true : savedState === "true";
    } catch (error) {
        isHidden = true;
    }

    function applyState(hidden) {
        var shouldHide = mediaQuery.matches && hidden;
        if (shouldHide) {
            document.body.classList.add("mobile-subtitle-sidebar-hidden");
        } else {
            document.body.classList.remove("mobile-subtitle-sidebar-hidden");
        }
    }

    hideButton.addEventListener("click", function() {
        isHidden = true;
        applyState(isHidden);
        try {
            window.localStorage.setItem(storageKey, "true");
        } catch (error) {}
    });

    showButton.addEventListener("click", function() {
        isHidden = false;
        applyState(isHidden);
        try {
            window.localStorage.setItem(storageKey, "false");
        } catch (error) {}
    });

    var onViewportChange = function(event) {
        if (!event.matches) {
            document.body.classList.remove("mobile-subtitle-sidebar-hidden");
        } else {
            applyState(isHidden);
        }
    };

    if (typeof mediaQuery.addEventListener === "function") {
        mediaQuery.addEventListener("change", onViewportChange);
    } else if (typeof mediaQuery.addListener === "function") {
        mediaQuery.addListener(onViewportChange);
    }

    applyState(isHidden);
}
